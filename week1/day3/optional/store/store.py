class dojo_Store :
    store_name = "dojoStore"
    
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def price_update(self, percent_change, is_increased):
        if self.price > 25:
            self.price = (self.price / percent_change) *100
            return print(f"{self.name} is now {self.price}")
        # elif self.price < 25:
        #     self
 


food_potato = dojo_Store ("chicken_breast", 20, "chicken")

food_potato.price_update(20, 5)


