from nicegui import ui

count = 0
counter_label = ui.label(f"カウント: {count}")


def increment():
    global count
    count += 1
    counter_label.text = f"カウント: {count}"


ui.button("カウントアップ", on_click=increment)

ui.run()
