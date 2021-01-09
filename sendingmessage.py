from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.label import Label
from associations import screen_nav
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
import pyrebase
from datetime import datetime
from kivymd.uix.menu import MDDropdownMenu
import json
import requests
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



class Message_sending(Screen):
    url = 'https://file-uploading-2e4d3-default-rtdb.firebaseio.com/.json'
    msgtxt=ObjectProperty(None)
    teachermail=ObjectProperty(None)
    remail=ObjectProperty(None)
    tnow = datetime.now()

    def patch(self, JSON):

        data ={'Message':self.msgtxt,'From':self.remail,'To':self.teachermail,'Date':self.tnow.strftime("%d%m%y, %H:%M:%S")}

        to_database = json.loads(JSON)
        requests.patch(url=self.url, json=to_database)


    def post(self, JSON):
        to_database = json.loads(JSON)
        requests.post(url=self.url[:-5], json=to_database)

    def printtxt(self):
        email = str(self.emailtxt.text)
        data = {'message': self.msgtxt.text, 'Email': self.emailtxt.text,
                    'Date': self.tnow.strftime("%m/%d/%Y, %H:%M:%S")}
        db.child('Message/Apeal').child(email.split("@")[0]).set(data)

        pass



class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Blue'
        screen=Builder.load_string(screen_nav)
        return screen


if __name__=='__main__':
        MyApp().run()
