from kivy.app import App

from Game import Game

class KivyApp(App):
    game = Game()

    def build(self):
        return self.game

KivyApp().run()
