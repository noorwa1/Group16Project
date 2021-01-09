from kivy.app import App
from kivy.lang import Builder
import json
import requests

KV = Builder.load_string ("""
ScreenManager:
    id: manager
    Screen:
        BoxLayout:
            orientation: 'vertical'
            GridLayout:
                cols:1
                Label:
                    text: 'Write a JSON string'
                TextInput:
                    size_hint_y: .2
                    id: JSON
            GridLayout:
                cols:1
                Button:
                    text: 'Patch Line'
                    on_press: app.patch(JSON.text)
                    on_release:
                        app.exit()
                Button:
                    text: 'Post Line'
                    on_press: app.post(JSON.text)
                    on_release:
                        app.exit()
                Button:
                    text: 'Put Line'
                    on_press: app.put(JSON.text)
                    on_release:
                        app.exit()
                
""")
#{"Student":{"Apeal":}}
class MyApp(App):

    url = 'https://file-uploading-2e4d3-default-rtdb.firebaseio.com/.json'

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)

    def post(self, JSON):
        to_database = json.loads(JSON)
        requests.post(url = self.url, json = to_database)

    def put(self, JSON):
        to_database = json.loads(JSON)
        requests.put(url = self.url, json = to_database)

    def exit(self):
        return exit()


    def build(self):
        return KV
if __name__ == '__main__':
    MyApp().run()
