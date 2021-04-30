from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.widget import Widget

class Player(Widget):
    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)
        self.winWidth, self.winHeight = Window.size

        self.spriteSource = "atlas://spritesheet/"

        self.spriteId = "down"

        self.redraw = True

        self.x = x
        self.y = y
        self.draw()

    def draw(self):
        windowWidth, windowHeight = Window.size

        if windowWidth != self.winWidth or windowHeight != self.winHeight:
            self.winWidth = windowWidth
            self.winHeight = windowHeight
            self.redraw = True

        # Do not redraw if unnecessary
        if not self.redraw:
            return

        # Redraw logic
        self.redraw = False

        self.canvas.clear()

        with self.canvas:
            Rectangle(source=self.spriteSource + self.spriteId, size=(windowWidth/15, windowHeight/10),
                      pos=(self.x * (windowWidth / 15), self.y * (windowHeight / 10)))

    def move(self, direction):
        self.redraw = True
        if direction == "w":
            self.y = self.y + 1
            self.spriteId = "up"
        if direction == "a":
            self.x = self.x - 1
            self.spriteId = "left"
        if direction == "s":
            self.y = self.y - 1
            self.spriteId = "down"
        if direction == "d":
            self.x = self.x + 1
            self.spriteId = "right"