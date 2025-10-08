class Item:
    # Constructor
    def __init__(self,name,description,price,stock_lvl):
        self.name = name
        self.description = description
        self.price = price
        self.stock_lvl = stock_lvl
    def stock_update(self,new_stock_lvl):
        self.stock_lvl = new_stock_lvl