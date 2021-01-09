from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from association import screen_nav

from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
import pyrebase
from datetime import datetime
from kivymd.uix.menu import MDDropdownMenu
from typing import List


firebaseConfig = {
    'apiKey': "AIzaSyAxS1KDjH4OQrbw-k050yGJHQ8giCuyFDU",
    'authDomain': "project16-f346d.firebaseapp.com",
    'databaseURL': "https://file-uploading-2e4d3-default-rtdb.firebaseio.com",
    'projectId': "project16-f346d",
    'storageBucket': "project16-f346d.appspot.com",
    'messagingSenderId': "237946682699",
    'appId': "1:237946682699:web:59b0610e150f5c42b7bcce",
    'measurementId': "G-W8TSC422XT"}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


class Apeal_Message(Screen):
    msgtxt = ObjectProperty(None)
    emailtxt = ObjectProperty(None)
    tnow = datetime.now()

    def printtxt(self):
        email = str(self.emailtxt.text)
        data = {'apeal': self.msgtxt.text, 'Email': self.emailtxt.text,
                'Date': self.tnow.strftime("%m/%d/%Y, %H:%M:%S")}
        db.child('apeal').child(email.split("@")[0]).set(data)
    pass



class school(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_nav)
        return screen

    def navigation_draw(self):
        print("navigation")


school().run()
