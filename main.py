# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


class TitleFunction(GridLayout):
    def __init__(self, **kwargs):
        self.appName = Label(text="CSC265 Messaging App", width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.settings = Button(text="Settings", width=Window.size[0] * 0.1, size_hint_y=None, multiline=False)
        self.returns = Button(text="Return", width=Window.size[0] * 0.1, size_hint_y=None, multiline=False)
        self.settings.bind(on_press=self.settings)
        self.returns.bind(on_press=MainMenu())

        topline = GridLayout(cols=1)
        topline.add_widget(self.settings)
        topline.add_widget(self.appName)
        topline.add_widget(self.returns)
        self.add_widget(topline)


class MainMenu(GridLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.cols = 2  # The Number of columns in grid is set

        self.add_widget(TitleFunction())
        # Sets the apps title box

        self.messagePreview = Label(text="Messages")  # Will load file for the messages saved locally
        self.add_widget(self.messagePreview)


class ChatMenu(GridLayout):
    def __init__(self, **kwargs):
        super(ChatMenu, self).__init__(**kwargs)

        self.cols = 3  # The Number of columns in grid is set
        self.rows = 3

        topline = self.add_widget(TitleFunction())
        # Sets the apps title box and app functions

        self.messagePreview = Label()  # Will load a txt file of saved files
        self.add_widget(self.messagePreview)
        # Load the message Preview

        self.newMessage = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.sendMessage)
        messageline = GridLayout(cols=3)
        messageline.add_widget(self.newMessage)
        messageline.add_widget(self.send)
        self.add_widget(messageline)
        # shows the user text input and send button


class Homepage(App):  # runs the homepage
    def build(self):
        return Label(MainMenu)


if __name__ == "__main__":
    Homepage().run()
