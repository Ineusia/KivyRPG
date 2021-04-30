from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Map(Widget):
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

        self.draw()

    def draw(self):
        window_width, window_height = Window.size

        #self.canvas.clear()
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                with self.canvas:
                    Rectangle(source='atlas://spritesheet/frame' + self.tiles[y][x], size=(window_width / 15, window_height / 10), pos=(x * window_width / 15, y * window_height / 10))

        #self.add_widget(Label(text=str(window_width)))

