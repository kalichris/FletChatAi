import sys 

from chataiM import *
import flet as ft 
from flet import *
from flet_core.control_event import ControlEvent                          
from math import pi 
import time

class Chat(UserControl):
    def __init__(self,page):
        self.page=page
        self.page.title='ChatAi'
        self.page.bgcolor="#23252e"
        self.page.scroll="auto"
        self.page.vertical_alignment= MainAxisAlignment.CENTER 
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.theme_mod=ThemeMode.DARK
        self.page.window_max_height=900
        self.page.window_height=900
        self.page.window_width=700
        self.page.window_max_width=700
        def InputCheckValue(e):
            inputValue=self.page.controls[2].content.controls[0].controls[0].value
            buttonSend=self.page.controls[2].content.controls[0].controls[1]
            print(inputValue)
            

          
        def sendMsg(e):
            msg=self.page.controls[2].content.controls[0].controls[0].value
            self.page.controls[2].content.controls[0].controls[0].clean()
            self.page.update()
                        
            if msg!="":
                chat=self.page.controls[1]
                chat.controls.append(Container(
                    bgcolor="transparent" ,
                    border_radius=10 ,
                    width=650,

                    border=ft.border.all(1, "#f1f1f2"),

                    content=Text(f"send : \n\t\t\t\t\t\t {msg}",
                    color="#ffffff"),
                    padding=padding.only(top=10,left=15,right=10,bottom=10))
                )
                self.page.update()
                replay=ChatAi().sendAi(msg)
            
                print(replay)
                

                chat.controls.append(Container(
                    bgcolor="transparent" ,
                    border_radius=10 , 
                    width=650,
                    border=ft.border.all(1, "#f1f1f2"),

                    content=Text(f" replay : \n\t\t\t\t\t\t {replay}",
                    color="#ffffff")
                    ,padding=10)
                )
                self.page.update()
            

            #Text(ChatAi(msg))
        self.page.add(
            AppBar(
                leading_width=100,
                title=Text("Chat AI",
                    size=32,
                    color="#FFFFEE", 
                    text_align="start",
                    weight=FontWeight.BOLD,
                ),
                center_title=False,
                toolbar_height=75,
                bgcolor="#3476e6"

            ),
            Column( 
                [
                   
                ] ,tight=True,
            ),
        
            Container(
                content=Column(
                controls=[
                    
                Row(
                    [
                        TextField(
                            width=550,
                            height=50,
                            border_color="#292c37",
                            cursor_color="#FFFFFEE",
                            bgcolor="transparent",
                            color="#FFFFEE",
                            border_radius=10,
                            autofocus=True,
                            shift_enter=True,
                            filled=True,
                            expand=True,
                            hint_text="Enter your message",
                            hint_style=TextStyle(
                                size=11,
                                color="#e7e7e7"
                            ),
                            on_change=InputCheckValue
                        ),
                        IconButton(
                            icon=icons.SEND,
                            icon_color="#3476e6",
                            icon_size=45,
                            tooltip="Send Message",
                            on_click=sendMsg,
                            disabled=False,
                           

                        )
                    ],spacing=5,alignment=MainAxisAlignment.CENTER
                )
            ]),margin=margin.only(top=750))
        )
    
        #print(self.page.controls[1].content.controls[1].controls)
# def main(page:ft.Page):
#     Chat(page)
# ft.app(target=main,port=5000,view=ft.AppView.WEB_BROWSER)