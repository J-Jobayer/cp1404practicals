"""
CP1404/CP5632 Practical
Kivy GUI program to display dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to create labels dynamically."""

    def __init__(self, **kwargs):
        """Initialise the app with some example data."""
        super().__init__(**kwargs)
        # You can change these to any data you like
        self.names = ["Bob Brown", "Mary Smith", "John Doe", "Jane Citizen"]

    def build(self):
        """Build the Kivy app from the kv file and create labels."""
        Window.size = (300, 200)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the main BoxLayout."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main_box.add_widget(temp_label)


DynamicLabelsApp().run()
