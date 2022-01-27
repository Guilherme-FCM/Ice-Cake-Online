from classes.Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = {}, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors
        
    def show_flavors(self):
        for sabor, attrs in self.flavors.items():
            print(f'| {sabor} | {attrs["estoque"]} | {attrs["preco"]} |')