from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Main_Page(BoxLayout):
    def __init__(self, **kwargs):
        super(Main_Page, self).__init__(**kwargs)

        self.orientation = "horizontal"
        self.box()

    def box(self):
        b1 = Button(text = "a")
        self.add_widget(b1)


# Boiler plate

class myApp(App):
    def build(self):
        return Main_Page()


if __name__ == "__main__":
    myApp().run()