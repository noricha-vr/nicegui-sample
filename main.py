from nicegui import ui
import os
from pathlib import Path
from dotenv import load_dotenv
import chat  # chat.pyをインポート
import countup  # countup.pyもインポート（同じディレクトリにあると仮定）

# .envファイルが存在する場合は読み込む
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    print("Warning: .env file not found. Please create one based on .env.example")

# OpenAI APIキーが設定されているか確認
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not set. AI features will not work correctly.")

# メインアプリケーションの設定
ui.run(title='NiceGUI Sample with AI Chat', port=8081) 
