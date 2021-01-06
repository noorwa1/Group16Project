import kivy
import pyrebase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class Filechooser(BoxLayout):
    def select(self, *args):
        firebaseconfig = {'apiKey': "AIzaSyBWUU7eIQD13XhdWc07ZcmbtOPwu4kkYbM",
                          'authDomain': "file-uploading-2e4d3.firebaseapp.com",
                          'projectId': "file-uploading-2e4d3",
                          'storageBucket': "file-uploading-2e4d3.appspot.com",
                          'messagingSenderId': "420295748286",
                          'appId': "1:420295748286:web:cb3f00a77a022b4fedccef",
                          'measurementId': "G-DHDSH9ST86"}
        firebase = pyrebase.initialize_app(firebaseconfig)
        storage = firebase.storage()
        cloud_file_name = "files/Uploaded"
        filename = args[1]
        storage.child(cloud_file_name).put(filename)
        try:

            self.label.text = args[1][0]


        except:
            pass


class FileApp(App):
    def build(self):
        return Filechooser()

    # run the App

if __name__==("__main__"):
    FileApp().run()
