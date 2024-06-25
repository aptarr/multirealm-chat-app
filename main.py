import flet as ft
from pages.login import login
from pages.register import register
from pages.dashboard import dashboard

def main(page: ft.Page):
    page.title = "Chat Application"
    page.window.width = 360
    page.window.height = 640
    page.window.title_bar_hidden = False
    
    routes = {
        "/login": login,
        "/register": register,
        "/dashboard": dashboard,
    }
    
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                e.route,
                [routes[e.route]()]
            )
        )
        page.update()
    
    page.on_route_change = route_change
    page.go("/login")

ft.app(main)