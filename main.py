from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Define the screen classes
class Home(Screen):
    pass

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class Screen4(Screen):
    pass

class Screen5(Screen):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_file('cqf.kv')

if __name__ == "__main__":
    MyApp().run()