import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget


class interfaceApp(App):

    def build(self):
        return Label()


main = interfaceApp()
main.run()
