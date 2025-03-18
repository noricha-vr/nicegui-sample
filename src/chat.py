from nicegui import ui

messages = []
chat_container = None
user_input = None


def send_message():
    if user_input.value.strip():
        messages.append({"user": "You", "text": user_input.value})
        display_messages()
        user_input.value = ""


def display_messages():
    chat_container.clear()
    for msg in messages:
        with chat_container:
            with ui.card().classes('w-full'):
                ui.label(f"{msg['user']}:").classes('font-bold')
                ui.label(f"{msg['text']}")


@ui.page('/chat')
def chat_page():
    global chat_container, user_input
    
    with ui.column().classes('w-full max-w-3xl mx-auto'):
        ui.label('チャット').classes('text-2xl font-bold')
        
        chat_container = ui.column().classes('w-full h-96 overflow-y-auto p-4 bg-gray-100 rounded')
        
        with ui.row().classes('w-full'):
            user_input = ui.input(placeholder='メッセージを入力').classes('flex-grow')
            ui.button('送信', on_click=send_message)
            
        user_input.on('keydown.enter', send_message)
        
        with ui.row().classes('w-full'):
            ui.link('カウンターページへ', '/countup').classes('mt-4') 
