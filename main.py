from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello World! Mera App Taiyaar Hai')

if __name__ == '__main__':
    MyApp().run()
[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
android.archs = arm64-v8a
