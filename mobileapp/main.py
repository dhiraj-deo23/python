import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import random
import glob
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "signup_screen"

    def log_in(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            if uname and pword and uname in users and users[uname]['password'] == pword:
                self.manager.current = "login_screen_success"
            else:
                self.ids.login_wrong.text = "Either or both of Username and password is wrong"


class RootWidget(ScreenManager):
    pass


class SignupScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            data = {"username": uname, "password": pword,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
            try:
                users = json.load(file)
                users[uname] = data
            except:
                users = {uname: data}
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "signup_screen_success"

    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class SignupScreenSuccess(Screen):
    def go_login(self):
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.current = "login_screen"

    def enlighten_mood(self, mood):
        mood = mood.lower()
        file_list = glob.glob("quotes/*.txt")
        files = [Path(fi).stem for fi in file_list]

        if mood in files:
            with open(f"quotes/{mood}.txt", encoding="utf-8") as file:
                quote = file.readlines()
                # self.ids.jokes.text = quote[randint(0, len(quote) - 1)]
                self.ids.jokes.text = random.choice(quote)
        else:
            self.ids.jokes.text = "sorry, wrong entry!"


class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
