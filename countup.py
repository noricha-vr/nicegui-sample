from nicegui import ui
from fastapi.responses import RedirectResponse

count = 0
counter_label = ui.label(f"カウント: {count}")


def increment():
    global count
    count += 1
    counter_label.text = f"カウント: {count}"


# カウンターページのルート
@ui.page('/countup')
def countup_page():
    global counter_label
    
    with ui.column().classes('w-full max-w-3xl mx-auto'):
        ui.label('カウンター').classes('text-2xl font-bold')
        
        counter_label = ui.label(f"カウント: {count}").classes('text-xl')
        ui.button("カウントアップ", on_click=increment)
        
        with ui.row().classes('w-full'):
            ui.link('チャットページへ', '/chat').classes('mt-4')


# ルートディレクトリにアクセスしたらカウンターページにリダイレクト
@ui.page('/')
def index():
    return RedirectResponse('/countup')
