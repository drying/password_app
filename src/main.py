import flet as ft
import secrets
import string

def main(page: ft.Page):
    # ページの設定
    page.title = "パスワード生成・管理アプリ"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 400

    # パスワード表示フィールド
    password_field = ft.TextField(label="Password", text_size=20, read_only=True, expand=True)
    
    # パスワード生成ロジック
    def generate_password(password_length):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(password_length))

    # 生成ボタンを押したときの処理
    def on_gererate_click(e):
        password_field.value = generate_password(password_length)
        page.update()
    
    # コピーボタンを押したときの処理
    async def copy_button_click(e):
        if not password_field.value:
            page.show_dialog(ft.SnackBar("パスワードがまだ生成されていません！"))
        else:
            await ft.Clipboard().set(password_field.value)
            page.show_dialog(ft.SnackBar("パスワードがコピーされました！"))

    # パスワード文字数スライダー
    password_length = 12

    def password_number_changed(e):
        nonlocal password_length
        password_length = int(e.control.value)
        lenght_label.value = f"長さ: {password_length}"
        page.update()

    lenght_label = ft.Text(f"長さ: {password_length}")
    slider = ft.Slider(min=8, max=20, divisions=12, value=password_length, on_change=password_number_changed)

    page.add(
        ft.Column(
            controls=[
                ft.Row(controls=[lenght_label, slider]),
            ],
        ),
        ft.Row(
            controls=[
                password_field,
                ft.Button(content="生成", width=120, on_click=on_gererate_click),
                ft.Button(content="コピー", width=120, on_click=copy_button_click),
            ]
        )
    )

ft.run(main)