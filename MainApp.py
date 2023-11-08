import flet as ft 
from flet import *
from page.login import *
from page.chat import *



# class Main(UserControl):
#     def __init__(self,page):
#         super().__init__()
#         page.padding = 0
#         self.page = page
#         self.init()
#         print(1)
#         self.on_route()
#     def on_route(self,route):
#         print(self.page.route)
#         print(1)
#     def init(self):
#         pages={
#             "/":Login(self.page),
#             "/login":Login(self.page),
            
#         }[self.page.route](self.page)
#         self.page.views.clear()
#         self.page.views.append(
#             View(route, [pages])
#         )
#         p
#         self.page.go("/login")

def main(page:ft.Page):
    print("Starting .........")
    def fn_views(page):
        return {
            "/login":View(
                route="/",
                controls=[
                    Login(page)
                ]
            )
        }

    # def fn_ruote_change(route):
    #     print(page.route)
    #     page.views.clear()
    #     page.views.append(fn_views(page)[page.route]

    #     )

    #     print("Views....")
    # page.on_route_change=fn_ruote_change
   
    page.go("/login")

    
    page.views.append(fn_views(page))
    page.update() 
    print(page.pwa)
    

ft.app(target=main,port=3000,view=ft.AppView.WEB_BROWSER)