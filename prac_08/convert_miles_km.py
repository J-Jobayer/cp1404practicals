"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Lindsay Ward"

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """Kivy app to convert miles to kilometres."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("miles_to_km.kv")
        return self.root

    def handle_calculate(self):
        """Handle calculation from button press, output result to label."""
        miles = self.get_miles()
        kilometres = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{kilometres:.3f}"

    def handle_increment(self, change):
        """Increase or decrease the miles value by 'change', then recalculate."""
        miles = self.get_miles() + change
        if miles < 0:
            miles = 0
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_miles(self):
        """Get the miles value from the text input, or 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesToKmApp().run()
