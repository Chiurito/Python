from kivymd import *

KV = """
Screen:
    MDRectangleFlatButton:
        text: "Hello Kivy World!"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""


class Builder:
    pass


class MDApp:
    pass


class MainApp(MDApp):

    def build(self):
        self.title = "Hello Kivy"
        self.theme_cls.theme_style = "Dark"  # Light
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)


MainApp().run()
