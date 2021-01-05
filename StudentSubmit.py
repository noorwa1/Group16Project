import pyrebase
import tkinter as tk
from tkinter import filedialog
global filename
config={
    'apiKey': "AIzaSyBWUU7eIQD13XhdWc07ZcmbtOPwu4kkYbM",
    'authDomain': "file-uploading-2e4d3.firebaseapp.com",
    'projectId': "file-uploading-2e4d3",
    'storageBucket': "file-uploading-2e4d3.appspot.com",
    'messagingSenderId': "420295748286",
    'appId': "1:420295748286:web:cb3f00a77a022b4fedccef",
    'measurementId': "G-DHDSH9ST86"
}

def UploadAction(event=None):

    filename= filedialog.askopenfilename()
    print('Selected:', filename)


firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
path_local=filename
path_on_cloud="Files/FirstFile"
storage.child(path_on_cloud).put(path_local)
root = tk.Tk()
button = tk.Button(root, text='Submit', command=UploadAction)
button.pack()

root.mainloop()
