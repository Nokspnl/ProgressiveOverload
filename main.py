# Define imports
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Defining the variable parameters of the program
Split = [
    "Chest, Triceps, Quads A",
    "Biceps, Back, Hams A",
    "Chest, Triceps, Shoulders ",
    "Chest, Triceps, Quads B",
    "Biceps, Back Hams B",
]


# Define the function we will call to switch between screens
def switch_screen(instance):
    app = App.get_running_app()
    # Get the text of the button clicked
    button_text = instance.text
    # Convert text to lowercase and remove spaces to match screen names
    screen_name = button_text
    # Switch to the corresponding screen
    app.root.current = screen_name


# Define the HomeScreen Class which inherits the methods and properties of the Screen Class
class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        home_box = BoxLayout(orientation="vertical")

        # Add Buttons
        for day in Split:
            day_button = Button(text=day, font_size=20)
            # Bind the button to switch to the corresponding screen
            day_button.bind(on_press=switch_screen)
            home_box.add_widget(day_button)

        self.add_widget(home_box)


# Define the ScreenManagement Class which inherits the methods and properties of the ScreenManager Class.
# This Class only manages Screen widgets (pre defined or ones we create ourselves).
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(Home(name="Home"))

        # Add each Screen to the ScreenManager
        for day in Split:
            screen_name = day
            screen = Screen(name=screen_name)
            # Outer BoxLayout
            outer_layout = BoxLayout(orientation="vertical")
            screen.add_widget(outer_layout)
            # Label
            label = Label(text=day, font_size=20)
            outer_layout.add_widget(label)
            # Inner GridLayout for text inputs
            inner_grid = GridLayout(cols=4, spacing=10)
            outer_layout.add_widget(inner_grid)
            # Populate inner grid with TextInputs
            for _ in range(16):
                text_input = TextInput(text="", multiline=False)
                inner_grid.add_widget(text_input)
            # Home button
            home_button = Button(text="Home", font_size=16, size_hint=(1, 0.1))
            home_button.bind(on_press=switch_screen)
            outer_layout.add_widget(home_button)
            self.add_widget(screen)


# Define the main App class
class MyApp(App):
    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    MyApp().run()
