from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class Sonajori(App):
    def build(self):
        self.score = 0
        self.time_left = 30

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.title = Label(
            text="SONAJORI",
            font_size=38,
            bold=True
        )

        self.score_label = Label(
            text="Score: 0",
            font_size=32
        )

        self.timer_label = Label(
            text="Time: 30",
            font_size=25
        )

        self.tap_button = Button(
            text="TAP TO PLAY!",
            font_size=30,
            background_color=(0.5, 0.1, 0.9, 1)
        )

        self.tap_button.bind(on_press=self.tap)

        layout.add_widget(self.title)
        layout.add_widget(self.score_label)
        layout.add_widget(self.timer_label)
        layout.add_widget(self.tap_button)

        Clock.schedule_interval(self.update_timer, 1)
        return layout

    def tap(self, instance):
        if self.time_left > 0:
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.text = f"Time: {self.time_left}"
        else:
            self.tap_button.disabled = True
            self.tap_button.text = "GAME OVER!"

Sonajori().run()
