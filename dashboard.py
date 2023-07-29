import os
import sys
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

Window.size = (600, 400)

KV1 = '''
MDScreen:
    MDRaisedButton:
        text: "      URL OSINT      "
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.run_program()
        size_hint: 0.1, 0.1
    
    MDRaisedButton:
        text: "Username OSINT"
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.run_username()
        size_hint: 0.1, 0.1
    
    MDRaisedButton:
        text: "Web Search - Phone Lookup - IP Lookup"
        pos_hint: {"center_x": 0.5, "center_y": 0.40}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.run_osint()
        size_hint: 0.1, 0.1
'''

KV = '''
#:import CustomOverFlowMenu __main__.CustomOverFlowMenu


MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "ITMS 448 - 548 - OSINT Dashboard "
        use_overflow: True
        overflow_cls: CustomOverFlowMenu()
        right_action_items:
            [
            ["home", lambda x: app.exit_program()],
            ["message-star", lambda x: app.team_program()],
            ]

    MDLabel:
        text: ""
        halign: "center"

'''

class CustomOverFlowMenu(MDDropdownMenu):
    # In this class you can set custom properties for the overflow menu.
    pass


class Dashboard(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return (
            MDScreen(
                   Builder.load_string(KV1) , Builder.load_string(KV)
                )
                
            ) 
        
    
    def callback(self, instance_action_top_appbar_button):
        print(instance_action_top_appbar_button)

    def team_program(self):
        print("open team...")
        os.system("python team.py")
    
    def exit_program(self):
        print("Exiting the program...")
        sys.exit(0)
        
   
    def run_program(self):
        os.system('python link.py')

    def run_username(self):
        os.system('python SherlockGui.py')

    def run_osint(self):
        os.system('python osint.py')
        

Dashboard().run()