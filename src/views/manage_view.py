import flet as ft

def manage_view(page: ft.Page) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[ft.Text("パスワード管理画面", size=20)]
        ),
        expand=True
    )