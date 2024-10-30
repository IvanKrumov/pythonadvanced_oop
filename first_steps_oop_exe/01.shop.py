class Shop:
    def __init__(self, name, items) -> None:
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
