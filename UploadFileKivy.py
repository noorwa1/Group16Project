import kivy
import pyrebase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
class Filechooser(BoxLayout):
    def select(self, *args):

        try:

            self.label.text = args[1][0]


        except:
            pass
        filenameInCloud=str(random.random())
        firebaseconfig = {'apiKey': "AIzaSyBWUU7eIQD13XhdWc07ZcmbtOPwu4kkYbM",
                              'authDomain': "file-uploading-2e4d3.firebaseapp.com",
                              'projectId': "file-uploading-2e4d3",
                              'storageBucket': "file-uploading-2e4d3.appspot.com",
                          'databaseURL': "https://file-uploading-2e4d3-default-rtdb.firebaseio.com",
                              'messagingSenderId': "420295748286",
                              'appId': "1:420295748286:web:cb3f00a77a022b4fedccef",
                              'measurementId': "G-DHDSH9ST86"}
        firebase = pyrebase.initialize_app(firebaseconfig)
        cloud_file_name = "files/uploaded/"+filenameInCloud

        filename = args[1][0]
        storage = firebase.storage()
        if (args):
            storage.child(cloud_file_name).put(filename)
            exit()
class FileApp(App):
    def build(self):
        return Filechooser()

    # run the App

if __name__==("__main__"):
    FileApp().run()
