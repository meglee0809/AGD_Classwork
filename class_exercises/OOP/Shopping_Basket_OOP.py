#from Basket_item import Item
import warnings

class Item:
    # Constructor
    def __init__(self,name,description,price,stock_lvl):
        self.name = name
        self.description = description
        self.price = price
        self.stock_lvl = stock_lvl

    def stock_update(self,new_stock_lvl):
        self.stock_lvl = new_stock_lvl

#-------------------------------------------------------------------------------
class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items = {}  # A dictionary of all the items in the shopping basket: {item:quantity}
        self.checkout = False

    # A method to add an item to the shopping basket
    def addItem(self, item, quantity):
        if quantity > 0:
            # Check if the item is already in the shopping basket
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

            new_stock_lvl = (item.stock_lvl - quantity)
            #tests whether quantity is actually possible
            if new_stock_lvl >= 0:
                item.stock_update(new_stock_lvl)
            else:
                self.items[item] -= quantity
                raise ValueError(f"Invalid operation - Cannot add {quantity} of {item.name} — only {item.stock_lvl} in stock. :(")
        else:
            warnings.warn("Invalid operation - Quantity must be a positive number!")

    # A method to remove an item from the shopping basket (or reduce its quantity)
    def removeItem(self, item, quantity=0):
        if item in self.items:
            if quantity < self.items[item] and quantity > 0:
                # Reduce the required quantity for this item
                self.items[item] -= quantity
            elif quantity == self.items[item] or quantity > self.items[item]:
                # Remove the item
                warnings.warn("It has been removed from your shopping basket :)")
                self.items[item] = 0
            else:
                warnings.warn("Invalid operation - Quantity must be a positive number!")

            new_stock_lvl = (item.stock_lvl + quantity)
            item.stock_update(new_stock_lvl)


    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item, quantity):
        if quantity > 0 and quantity <= (item.stock_lvl + self.items[item]):
            new_stock_lvl = ((item.stock_lvl + self.items[item])- quantity)
            if new_stock_lvl >= 0:
                self.items[item] = quantity
                item.stock_update(new_stock_lvl)
            else:
                warnings.warn(f"Invalid operation - Cannot add {quantity} of {item.name} — only {item.stock_lvl} in stock. :(")
                self.items[item] = quantity

        elif quantity == 0:
            warnings.warn("It has been removed from your shopping basket :)")
            new_stock_lvl = (item.stock_lvl + self.items[item])
            item.stock_update(new_stock_lvl)
            self.items[item] = 0

        else:
            warnings.warn(f"Invalid operation - Cannot add {quantity} of {item.name} — only {item.stock_lvl} in stock. :(")


    # A method to view/list the content of the basket.
    def view(self):
        totalCost = 0
        print("---------------------")
        for item in self.items:
            quantity = self.items[item]
            if quantity > 0 :
                cost = quantity * item.price
                print(" + " + item.name + " - " + str(quantity) + " x £" + '{0:.2f}'.format(
                    item.price) + " = £" + '{0:.2f}'.format(cost))
                totalCost += cost
        print("---------------------")
        print(" = £" + '{0:.2f}'.format(totalCost))
        print("---------------------")

    # A method to calculate the total cost of the basket.
    def getTotalCost(self):
        totalCost = 0
        for item in self.items:
            quantity = self.items[item]
            cost = quantity * item.price
            totalCost += cost
        return totalCost

    # A method to empty the content of the basket
    def reset(self):
        self.items = {}


#Tests---------------------------------------------
tomatoSoup = Item("Tomato Soup","200mL can", 0.70,5)
spaghetti = Item("Spaghetti","500g pack", 1.10,4)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10,3)
mozarella = Item("Mozarella","100g", 1.50,2)
gratedCheese = Item("Grated Cheese","100g",2.20,1)


myBasket = ShoppingBasket()

#print(tomatoSoup.stock_lvl) should be 5
myBasket.addItem(tomatoSoup, 4)
#print(tomatoSoup.stock_lvl) should be 1
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
#myBasket.addItem(tomatoSoup, 6)

myBasket.removeItem(tomatoSoup, 3)
#print(tomatoSoup.stock_lvl) should be 4
myBasket.removeItem(tomatoSoup, 2364284)
#myBasket.view()
myBasket.updateItem(tomatoSoup, 2)

myBasket.view()
myBasket.reset()
