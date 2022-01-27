class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'Nome do Restaurante: {self.restaurant_name} \nTipo de Cozinha....: {self.cuisine_type} \nClientes Atendidos.: {self.number_served}')

    def open_restaurant(self):
        print(f'Nosso Restaurante {self.restaurant_name} está aberto! Entre!')
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, number = 1):
        self.number_served += number
    