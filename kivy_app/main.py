import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class myGrid(Widget):
    pass


class MyApp(App):
    def build(self):
        return myGrid()


if __name__ == '__main__':
    MyApp().run() 