import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen


KV1 = '''
MDScreen:
    MDRaisedButton:
        text: "Extract all the URLs from the Webpage"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.run_program()
        size_hint: 0.1, 0.1
    
    MDRaisedButton:
        text: "Facebook OSINT"
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.run_program()
        size_hint: 0.1, 0.1
    
    MDRaisedButton:
        text: "Twitter OSINT"
        pos_hint: {"center_x": 0.5, "center_y": 0.40}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.run_program()
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
            ["home", lambda x: app.callback(x), "Home", "Home"],
            ["message-star", lambda x: app.callback(x), "Message star", "Message star"],
            ["message-question", lambda x: app.callback(x), "Message question", "Message question"],
            ["message-reply", lambda x: app.callback(x), "Message reply", "Message reply"],
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
    def run_program(self):
        os.system('python link.py')


Dashboard().run()