from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

from Map import Map
from Player import Player

window_width = NumericProperty()
window_height = NumericProperty()

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set up Keyboard Listener
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.map = Map()
        self.add_widget(self.map)

        # Define our Player
        self.player = Player(3, 3)
        self.add_widget(self.player)

        Clock.schedule_interval(self.tick, 1 / 60)

    def tick(self, arg):
        global window_width
        global window_height

        window_width, window_height = Window.size

        self.map.draw()
        self.player.draw()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ["w", "a", "s", "d"]:
            self.player.move(keycode[1])
        return True
