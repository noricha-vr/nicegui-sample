from nicegui import ui
import os
import asyncio
import threading
import time
import nest_asyncio
from agents import Agent, Runner, WebSearchTool
from threading import Event

# イベントループの競合を解決
nest_asyncio.apply()

# OpenAI APIキーを設定（実際の使用時は環境変数から取得するなど安全な方法を使用）
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# AIエージェントの作成
chat_agent = Agent(
    name="Chat Assistant",
    instructions="あなたは役立つアシスタントです。ユーザーの質問に丁寧に答えてください。",
    tools=[WebSearchTool()],  # ウェブ検索ツールを追加
    model="gpt-4o-mini"  # 使用するモデルを指定
)

# グローバル変数
messages = []
chat_container = None
user_input = None
agent_result = None
result_ready = Event()  # スレッド間の通信用イベント

# 定期的にチェックするタイマーを設定するフラグ
timer_set = False


def send_message():
    global timer_set
    
    if user_input.value.strip():
        # ユーザーのメッセージを保存して表示
        user_message = user_input.value
        messages.append({"user": "You", "text": user_message})
        display_messages()
        user_input.value = ""
        
        # 「Thinking...」メッセージを表示
        thinking_msg = {"user": "Assistant", "text": "思考中..."}
        messages.append(thinking_msg)
        display_messages()
        
        # イベントをリセット
        result_ready.clear()
        
        # 定期チェック用タイマーを設定（まだ設定されていない場合）
        if not timer_set:
            ui.timer(0.5, check_agent_result)
            timer_set = True
        
        # 別スレッドでエージェントの処理を実行
        threading.Thread(target=run_agent_in_thread, args=(user_message, thinking_msg)).start()


def check_agent_result():
    """定期的に結果をチェックするタイマー関数"""
    if result_ready.is_set():
        process_agent_result()
        result_ready.clear()
    return True  # タイマーを継続


def run_agent_in_thread(user_message, thinking_msg):
    global agent_result
    
    try:
        # 新しいイベントループを作成して実行
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        
        # エージェントから応答を取得
        result = Runner.run_sync(chat_agent, user_message)
        
        # 結果を保存
        agent_result = {"success": True, "thinking_msg": thinking_msg, "response": result.final_output}
        
    except Exception as e:
        # エラー情報を保存
        agent_result = {"success": False, "thinking_msg": thinking_msg, "error": str(e)}
    
    finally:
        # 完了を通知
        result_ready.set()


def process_agent_result():
    global agent_result
    
    if agent_result:
        thinking_msg = agent_result["thinking_msg"]
        
        if agent_result["success"]:
            # 思考中メッセージを削除して、実際の応答を追加
            messages.remove(thinking_msg)
            messages.append({"user": "Assistant", "text": agent_result["response"]})
        else:
            # エラーメッセージを表示
            messages.remove(thinking_msg)
            messages.append({"user": "Assistant", "text": f"エラーが発生しました: {agent_result['error']}"})
        
        # 結果を使用したら初期化
        agent_result = None
        
        # メッセージを更新
        display_messages()


def display_messages():
    chat_container.clear()
    for msg in messages:
        with chat_container:
            with ui.card().classes('w-full mb-2'):
                ui.label(f"{msg['user']}:").classes('font-bold')
                ui.label(f"{msg['text']}").classes('whitespace-pre-wrap')


@ui.page('/chat')
def chat_page():
    global chat_container, user_input
    
    with ui.column().classes('w-full max-w-3xl mx-auto'):
        ui.label('AIアシスタントチャット').classes('text-2xl font-bold')
        
        with ui.card().classes('w-full mb-4 p-4 bg-blue-50'):
            ui.label('このチャットはOpenAI Agent SDKを使用しています。インターネット検索機能も利用できます。')
        
        chat_container = ui.column().classes('w-full h-96 overflow-y-auto p-4 bg-gray-100 rounded')
        
        with ui.row().classes('w-full'):
            user_input = ui.input(placeholder='メッセージを入力...').classes('flex-grow')
            ui.button('送信', on_click=send_message).classes('bg-blue-500 text-white')
            
        user_input.on('keydown.enter', send_message)
        
        with ui.row().classes('w-full'):
            ui.link('カウンターページへ', '/countup').classes('mt-4')
            
        # 初期メッセージを表示
        if len(messages) == 0:
            messages.append({"user": "Assistant", "text": "こんにちは！どのようにお手伝いできますか？"})
            display_messages() 
