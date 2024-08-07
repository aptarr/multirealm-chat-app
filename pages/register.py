import flet as ft
from cli import cc

def register():
    def handle_register(e):
        username = username_field.value
        password = password_field.value
        confirm = confirm_field.value

        if password == confirm:
            result = cc.proses(f"register {username} {password}")
            
            if result.startswith('username'):
                e.page.go("/dashboard")
            else:
                status.value = result
                e.page.update()
        else:
            status.value = 'Confirm password salah'
            e.page.update()
            
    logo = ft.Container(
        content = ft.Image(src="img/logo.png", width=100, height=100),
        alignment = ft.alignment.center,
        margin = ft.margin.only(bottom=30, top=0)
    )
    username_field = ft.TextField(
        label="Username", 
        width=300, 
        height=40, 
        bgcolor="#d84d4d, 0.2", 
        border_radius=15, 
        border_color=ft.colors.TRANSPARENT, 
        filled=True
    )
    password_field = ft.TextField(
        label="Password", 
        password=True, 
        width=300, 
        height=40, 
        bgcolor="#d84d4d, 0.2", 
        border_radius=15, 
        border_color=ft.colors.TRANSPARENT, 
        filled=True
    )
    confirm_field = ft.TextField(
        label="Confirm Password", 
        password=True, 
        width=300, 
        height=40, 
        bgcolor="#d84d4d, 0.2", 
        border_radius=15, 
        border_color=ft.colors.TRANSPARENT, 
        filled=True
    )
    register_button = ft.ElevatedButton(
        text="Register", 
        on_click=handle_register, 
        width=300, 
        height = 40,
        bgcolor="#d84d4d", 
        color=ft.colors.WHITE
    )
    login_row = ft.Row(
        controls=[
            ft.Text("Have an account?", size=12),
            ft.TextButton(text="Login", on_click=lambda e: e.page.go("/login"))
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    status = ft.Text()
    
    return ft.Column(
        controls = [
            ft.Container(height=90),
            logo,
            username_field,
            password_field,
            confirm_field,
            ft.Container(height=30),
            register_button,
            login_row,
            status
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )