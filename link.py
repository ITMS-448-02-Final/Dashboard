import kivy
import os
import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
from bs4 import BeautifulSoup

from kivy.core.window import Window
from kivy.uix.button import Button



Window.size = (600, 100)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text=" WebSite Target : ", size_hint_x=None, width=300))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.login)
        self.add_widget(self.submit)


    def login(self, instance):
        name = self.name._get_text()
        grab = requests.get(name)
        soup = BeautifulSoup(grab.text, 'html.parser')

        f = open("get-link.txt", "w")
        # traverse paragraphs from soup
        for link in soup.find_all("a"):
            data = link.get('href')
            f.write(data)
            f.write("\n")
        f.close()



class Link(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    Link().run()