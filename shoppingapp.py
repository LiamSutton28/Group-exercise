from product import Product
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

TOTAL_PRICE = 0


class ShoppingApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.guitars = [Product("Cheese", 12.5),
                        Product("Laptop", 912.95),
                        Product("Plant", 4.75), ]

    def build(self):
        """Build the Kivy GUI."""
        Window.size = 1000, 800
        self.title = "Kivy + Classes = Products"
        self.root = Builder.load_file("shopping_list.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.status_text = f"Total price: {TOTAL_PRICE}"
        for product in self.products:
            temp_button = Button(text=str(product))
            temp_button.bind(on_release=self.press_entry)
            temp_button.product = product
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        product = instance.product
        instance.text = str(product)
        product.price += TOTAL_PRICE

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entries_box.children:
            instance.state = 'normal'
        self.status_text = ""


