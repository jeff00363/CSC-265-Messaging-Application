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
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


class ConnectionInfo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # user sets the input for the ip address
        self.add_widget(Label(text="IP ADDRESS: "))
        self.ipAddress = TextInput(multiline=False)
        self.add_widget(self.ipAddress)

        # user sets the input for the port address
        self.add_widget(Label(text="PORT NUMBER: "))
        self.portNumber = TextInput(multiline=False)
        self.add_widget(self.portNumber)

        # user sets the input for the username
        self.add_widget(Label(text="NAME: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # user sets the input button to join a chat and runs the script
        self.add_widget(Label(text="JOIN CHAT: "))
        self.connectBTN(Button("CONNECT"))
        self.join.bind(on_press=self.click)
        self.add_widget(self.connectBTN)

    def click(self, instance):  # This function will save the data from the input to variables
        Clock.schedule_once(self.connect, 1)

        ipa = self.ipAddress.text
        portn = self.portNumber.text
        user = self.username.text

        # print(f"{user} is connecting to {ipa} at port {portn} ")
        with open("connections.txt", "w") as f:
            f.write(f"{user},{ipa},{portn}")
        info = f"Connecting {user} to {ipa}:{portn} "
        dataPage.info_page.update_info(info)


class dataPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.data = Label(halign="center", valign="middle", font_size=30)
        self.add_widget(self.message)

    def updateData(self, textData):
        self.data.text = textData


class messageDisplay(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)

        self.messagesOld = Label(size_hint_y=None, markup=True)
        self.layout.add_widget(self.messagesOld)

    def updateMessages(self, messages):
        self.history(self, messages)
        self.layout.height = self.messagesOld.texture_size[1] + 10
        self.history.height = self.messagesOld.texture_size[1]

        self.scroll_to(self.scroll_to_point)

class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2

        self.history = Label(height=Window.size[1] * 0.9, size_hint_y=None)
        self.add_widget(self.history)

        self.message = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.sendBTN = Button(text="Send")
        self.sendBTN.bind(on_press=self.sendBTN)

        inputLine = GridLayout(cols=2)
        inputLine.add_widget(self.message)
        inputLine.add_widget(self.sendBTN)
        self.add_widget(inputLine)


class HomepageLogin(App):  # runs the homepage and login
    def build(self):
        self.display = ScreenManager()

        self.connect = ConnectionInfo()
        mains = Screen(name="Connect Data")
        mains.add_widget(self.connect)
        self.display.add_widget(mains)

        self.dataprep = dataPage()
        mains = Screen(name="Data Processing")
        mains.add_widget(self.dataprep)
        self.display.add_widget(mains)
        return self.display



    def create_chat_page(self):
        self.chatPage = ChatPage()
        mains = Screen(name='Chat')
        mains.add_widget(self.chatPage)
        self.display.add_widget(mains)


def errors(message):
    mains = Screen(name="ERROR")
    mains.add_widget(Label("Error"))


if __name__ == "__main__":
    txttotxt = HomepageLogin()
    txttotxt.run()
