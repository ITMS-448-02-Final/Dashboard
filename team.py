from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (600, 200)


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout()
        self.inside.cols = 4
        self.inside.add_widget(Label(text=" Ella Brady ", center_x=100, center_y=100, padding_x=30))
        self.inside.add_widget(Label(text=" Kevin Cain ", center_x=100, center_y=100, padding_x=30))
        self.inside.add_widget(Label(text=" Mahmood Mehrjoo ", center_x=100, center_y=100, padding_x=30))
        self.inside.add_widget(Label(text=" David Krahl ", center_x=100, center_y=100, padding_x=30))
        self.inside.add_widget(Label(text=" Suleman Jaffri ", center_x=100, center_y=100, padding_x=30))
        self.inside.add_widget(Label(text=" Jack Jarjourah ", center_x=100, center_y=100, padding_x=30))
        self.inside.add_widget(Label(text=" Rami Naser ", center_x=100, center_y=100, padding_x=30))
        self.add_widget(self.inside)


class Team(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    Team().run()