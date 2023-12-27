class Command:
    number_total_command = 0
    total_price = 0
    def __init__(self,id_buyer,id_item,quantity,price):
        self.__id_buyer = id_buyer
        self.__id_item = id_item
        self.__quantity = quantity
        self.__price = price
        Command.number_total_command += 1
        Command.total_price += self.get_price()
    def id_buyer(self):
        return self.__id_buyer
    def id_item(self):
        return self.__id_item
    def quantity(self):
        return self.__quantity
    def price(self):
        return self.__price
    def get_price(self):
        x = self.price() * self.quantity()
        return x
    def __str__(self):
        return f"{self.id_buyer()}, {self.id_item()} : {self.price()} * {self.quantity()} = {self.get_price()}"
    @classmethod
    def get_number_total_command(cls):
        return cls.number_total_command
    @classmethod
    def get_total_price(cls):
        return cls.total_price