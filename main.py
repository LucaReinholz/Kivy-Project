import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


"""class Touch(Widget):
    def on_touch_down(self, touch):
        #return super().on_touch_down(touch)
        pass

    def on_touch_move(self, touch):
        #return super().on_touch_move(touch)
        pass


    def on_touch_up(self, touch):
        #return super().on_touch_up(touch)
        pass
"""

class Grid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name:", self.name.text, "email:", self.email.text)
        self.name.text = ""
        self.email.text = ""


class TestApp(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    TestApp().run()