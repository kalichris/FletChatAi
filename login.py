import flet as ft 
from flet import *
from flet_core.control_event import ControlEvent
from page.chat  import *                  
from math import pi 
import time
import random
class BoxStyle(UserControl):
    def __init__(self,border_color,bgcolor,rotate):
        super().__init__()
        self.border_color=border_color
        self.bgcolor=bgcolor
        self.rotate=rotate
    def build(self):
        return Container(
            width=48,
            height=48,
            border=border.all(2.5,self.border_color),
            bgcolor=self.bgcolor,
            border_radius=2,
            rotate=transform.Rotate(self.rotate,alignment.center),
            animate_rotation=animation.Animation(700,"easeInOut")
        )

class InputStyle(UserControl):
    def __init__(self, name , text_hint, stat ,page):
        super().__init__()
        self.name=name
        self.text_hint=text_hint
        self.stat=stat 
        self.page=page

    def InputCheck(self,e):
        userIn=self.page.controls[0].content.content.controls[5].controls[0].controls[0].content.controls[1].value
        passwdIn=self.page.controls[0].content.content.controls[7].controls[0].controls[0].content.controls[1].value
        buttonIn=self.page.controls[0].content.content.controls[9].controls[0]
        if all([userIn,passwdIn]):
            buttonIn.disabled=False
        else:
            buttonIn.disabled=True
        self.page.update()

    def build(self):
        return Container(
                    width=300,
                    height=40,
                    border=border.only(bottom=border.BorderSide(.7,"white54")),
                    content=Row(spacing=20,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                                Icon(
                                    color="#FFFFEE",
                                    name=self.name,
                                    size=28,
                                    opacity=.85
                                ),TextField(
                                    border_color="transparent",
                                    bgcolor="transparent",
                                    color="#FFFFEE",
                                    height=20,
                                    cursor_width=10,
                                    width=260,
                                    text_size=16,
                                    content_padding=3,
                                    cursor_color="#FFFFFEE",
                                    hint_text=self.text_hint,
                                    hint_style=TextStyle(
                                        size=16,
                                        color="#FFFFEE"

                                    ),password=self.stat,
                                    can_reveal_password=self.stat,
                                    on_change=self.InputCheck
                                )
                            ]
                        )
                )
class Login(UserControl):
    def __init__(self,page):
        print(1)
        self.page=page
        self.page.title='Login ChatAi'
        self.page.bgcolor="#2c3240"
        self.page.vertical_alignment=MainAxisAlignment.CENTER 
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.theme_mod=ThemeMode.DARK
        self.page.window_max_height=900
        self.page.window_height=900
        self.page.window_width=470
        self.page.window_max_width=470
   
        
        def LoginBoutton(res):
            def fn_views(page):
                return {
                    "/chat":View(
                        route="/chat",
                        controls=[
                            Chat(page)
                        ]
                    )
                }
            def close_dlg(e):
                dlg_modal.open = False
                page.update()
            userIn=self.page.controls[0].content.content.controls[5].controls[0].controls[0].content.controls[1].value
            passwdIn=self.page.controls[0].content.content.controls[7].controls[0].controls[0].content.controls[1].value
            buttonIn=self.page.controls[0].content.content.controls[9].controls[0]
            if userIn == "admin" and passwdIn == "1234":
                
                dlg_modal = AlertDialog(
                    modal=True,
                    open=True,
                    title=Text("Registration succeeded",
                        weight=ft.FontWeight.BOLD,
                        color=colors.WHITE
                    ),
                    content=ft.Text(f"Welcame back : {userIn}"),
                    actions=[
                        ft.TextButton("Yes", on_click=close_dlg),
                    ]
                )
                
                self.page.dialog=dlg_modal
                self.page.update()
                #self.page.views.clear()
                self.page.go("/chat")
                #self.page.views.clear()
                self.page.views.append(fn_views(self.page))
                self.page.update()


            else:
            
                dlg_modal = AlertDialog(
                    modal=True,
                    open=True,
                    title=Text("Registration failed",
                        weight=ft.FontWeight.BOLD,
                        color=colors.WHITE
                    ),
                    content=ft.Text(f"Sorry, username or password incorrect"),
                    actions=[
                        ft.TextButton("Yes", on_click=close_dlg),
                    ]
                )
                self.page.dialog=dlg_modal
                self.page.update()

        def animationBox():
            x,y=pi/4,pi/4
            fristBox=self.page.controls[0].content.content.controls[1].controls[0].controls[0]
            secondBox=self.page.controls[0].content.content.controls[1].controls[1].controls[0]
            thirdBox=self.page.controls[0].content.content.controls[-1].controls[0].controls[0]
            fourthBox=self.page.controls[0].content.content.controls[-1].controls[1].controls[0]
            count=0
            while True : 
                if count >= 0 and count <= 4:
                    fristBox.rotate = transform.Rotate(x,alignment.center)
                    thirdBox.rotate = transform.Rotate(x,alignment.center)

                    secondBox.rotate = transform.Rotate(y,alignment.center)
                    fourthBox.rotate = transform.Rotate(y,alignment.center)

                    fristBox.update()
                    thirdBox.update()
                    secondBox.update()
                    fourthBox.update()

                    y += pi/2
                    x-= pi /2

                    count+=1
                    time.sleep(.75)
                if count >= 5 and count <= 10 :
                    y += pi/2
                    x-= pi /2

                    fristBox.rotate = transform.Rotate(x,alignment.center)
                    thirdBox.rotate = transform.Rotate(x,alignment.center)

                    secondBox.rotate = transform.Rotate(y,alignment.center)
                    fourthBox.rotate = transform.Rotate(y,alignment.center)
                    fristBox.update()
                    thirdBox.update()
                    secondBox.update()
                    fourthBox.update()
                    count+=1
                    time.sleep(.75)
                if count > 10:
                    count = 0

                
        self.page.add(
            Card(
                width=400,
                height=650,
                elevation=15,
                content=Container(
                    bgcolor="#303746",
                    border_radius=10,
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Divider(height=50,color="transparent"),
                            Stack(
                                controls=[
                                    BoxStyle("#FE5F55",None,pi/4),
                                    BoxStyle("#FFFFEE","#303746",pi * 2),
                                ]
                            ),Divider(height=10,color="transparent"),
                            Column([
                                Row([
                                    Text("Welcome",
                                        size=30,
                                        weight=FontWeight.BOLD,
                                        color="#FFFFEE",
                                    ),
                                    Text("Back",
                                        size=32,
                                        #bgcolor=ft.colors.BLACK,
                                        weight=FontWeight.BOLD,
                                        color="#FE5F55"
                                    )
                                ],spacing=0,alignment=MainAxisAlignment.CENTER
                                ) 
                            ]
                            ),Divider(height=50,color="transparent"),
                            Column([
                                InputStyle(icons.PERSON_ROUNDED,"UserName",False,page)
                            ]         
                            ),Divider(height=10,color="transparent"),
                            Column(
                                [
                                InputStyle(icons.LOCK_OUTLINE_ROUNDED,"Password",True,page)
                                ]
                            ),Divider(height=15,color="transparent"),
                            Column(
                                [
                                    ElevatedButton("Login",
                                            bgcolor="#323643",
                                            color="#FFFFEE",
                                            width=300,
                                            height=40,
                                            disabled=True,
                                            on_click=LoginBoutton,
                                            
                                        )
                                ]
                            ),Divider(height=70 ,color="transparent"),
                            Stack(
                                controls=[
                                    BoxStyle("#FE5F55",None,pi/4),
                                    BoxStyle("#FFFFEE","#303746",pi * 2),
                                    
                                ]
                            )
                ])
            )
                )
                
            )

            
        
        

        
    
        animationBox()
        
    #if __name__ == '__main__':
    # ft.app(target=main,port=8551,view=ft.AppView.WEB_BROWSER)
