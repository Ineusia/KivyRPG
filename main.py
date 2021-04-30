from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

class Map(Widget):
    window_width = NumericProperty()
    window_height = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tiles = [
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '4', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ]

        self.window_width, self.window_height = Window.size

        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                with self.canvas:
                    Rectangle(source='atlas://spritesheet/frame' + self.tiles[y][x], size=(self.window_width / 15, self.window_height / 10), pos=(x * self.window_width / 15, y * self.window_height / 10))
                #self.add_widget(self.rect);

        with self.canvas:
            Rectangle(source='atlas://spritesheet/walkdown', size=(self.window_width/15, self.window_height / 10), pos=(128, 128))

        self.label = Label(text=str(self.window_width))
        self.add_widget(self.label)

        Clock.schedule_interval(self.setVars, 1/60)

    def update(self):
        for index in range(len(self.canvas.children)):
            if isinstance(self.canvas.children[index], Rectangle):
                oldSize = self.canvas.children[index].size
                self.canvas.children[index].size = (self.window_width/15, self.window_height/10)

                ratioX = oldSize[0]/(self.window_width/15)
                ratioY = oldSize[1]/(self.window_height/10)

                oldPos = self.canvas.children[index].pos
                self.canvas.children[index].pos = (oldPos[0]/ratioX, oldPos[1]/ratioY)

        self.remove_widget(self.label)
        self.label = Label(text=str(self.window_width))
        self.add_widget(self.label)

    def setVars(self, value):
        oldWidth = self.window_width
        oldHeight = self.window_height
        self.window_width, self.window_height = Window.size

        if (oldWidth != self.window_width | oldHeight != self.window_height):
           self.update()


class GameScreen(Widget):
    pass

class KivyApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    KivyApp().run()