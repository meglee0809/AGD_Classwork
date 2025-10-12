import pytest
from class_exercises.OOP.Shopping_Basket_OOP import  Item, ShoppingBasket

#testing setup --------------------------------------------------------

@pytest.fixture
def setup_items_and_basket():
    # Create items
    tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, 20)
    spaghetti = Item("Spaghetti", "500g pack", 1.10, 20)
    blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, 20)
    mozarella = Item("Mozarella", "100g", 1.50, 20)
    gratedCheese = Item("Grated Cheese", "100g", 2.20, 29)

    # Create basket and add items
    basket = ShoppingBasket()
    basket.addItem(tomatoSoup, 4)
    basket.addItem(blackOlives, 1)
    basket.addItem(mozarella, 2)
    basket.addItem(tomatoSoup, 6)

    return basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese

def test_shopping_basket_setup(setup_items_and_basket):
    """ Test basket has been set up correctly """
    basket, tomatoSoup, *other = setup_items_and_basket
    assert basket.items[tomatoSoup] == 10
    assert tomatoSoup.stock_lvl == 10


#add item tests ----------------------------------------------

def test_add_more_than_stock(setup_items_and_basket):
    """ Test adding more items than exist in stock"""
    basket, tomatoSoup, *other = setup_items_and_basket
    # Raise an error if you try to add more items than exist in stock.
    with pytest.raises(ValueError):
        basket.addItem(tomatoSoup,4583824953245)

def test_add_neg_quantity(setup_items_and_basket):
    """ Test adding negative quantity items """
    basket, tomatoSoup, *other = setup_items_and_basket
    with pytest.warns(UserWarning):
        basket.addItem(tomatoSoup,-5)

def test_add_items_normal_data(setup_items_and_basket):
    """ Test adding items of normal data """
    basket, tomatoSoup, *other = setup_items_and_basket
    #adding less than stock
    basket.addItem(tomatoSoup,5)
    assert basket.items[tomatoSoup] == 15
    assert tomatoSoup.stock_lvl == 5

    #adding equal to stock
    basket.addItem(tomatoSoup,5)
    assert basket.items[tomatoSoup] == 20
    assert tomatoSoup.stock_lvl == 0


#remove item tests --------------------------------------------

def test_remove_items_normal_data(setup_items_and_basket):
    """ Test removing items of normal data"""
    basket, tomatoSoup, *other = setup_items_and_basket
    # removing less than basket amount
    basket.removeItem(tomatoSoup, 3)
    assert basket.items[tomatoSoup] == 7
    assert tomatoSoup.stock_lvl == 13

    # removing full basket amount
    basket.removeItem(tomatoSoup, 7)
    assert tomatoSoup.stock_lvl == 20
    with pytest.warns(UserWarning):
        basket.removeItem(tomatoSoup, 7)
    assert basket.items[tomatoSoup] == 0

def test_remove_items_more_than_quantity(setup_items_and_basket):
    """ Test removing items of more than quantity items """
    basket, tomatoSoup, *other = setup_items_and_basket
    basket.removeItem(tomatoSoup, 15)
    assert basket.items[tomatoSoup] == 0
    with pytest.warns(UserWarning):
        basket.removeItem(tomatoSoup, 15)

def test_remove_items_neg_quantity(setup_items_and_basket):
    """ Test removing negative quantity items """
    basket, tomatoSoup, *other = setup_items_and_basket
    with pytest.warns(UserWarning):
        basket.removeItem(tomatoSoup, -5)


#update item tests -----------------------
def test_update_items_normal_data(setup_items_and_basket):
    """ Test updating items of normal data """
    basket, tomatoSoup, *other = setup_items_and_basket
    basket, tomatoSoup, *other = setup_items_and_basket
    # adding less than stock
    basket.updateItem(tomatoSoup, 5)
    assert basket.items[tomatoSoup] == 5
    assert tomatoSoup.stock_lvl == 15

    # adding equal to stock
    basket.updateItem(tomatoSoup, 20)
    assert basket.items[tomatoSoup] == 20
    assert tomatoSoup.stock_lvl == 0

    #removing item by updating to 0
    basket.updateItem(tomatoSoup, 0)
    assert tomatoSoup.stock_lvl == 20
    with pytest.warns(UserWarning):
        basket.removeItem(tomatoSoup, 7)
    basket.updateItem(tomatoSoup, 0)
    assert basket.items[tomatoSoup] == 0

def test_update_items_more_than_quantity(setup_items_and_basket):
    """ Test updating items of more than quantity items """
    basket, tomatoSoup, *other = setup_items_and_basket
    with pytest.warns(UserWarning):
        basket.updateItem(tomatoSoup,748562938)

def test_update_neg_quantity(setup_items_and_basket):
    """ Test updating negative quantity items """
    basket, tomatoSoup, *other = setup_items_and_basket
    with pytest.warns(UserWarning):
        basket.updateItem(tomatoSoup,-5)


#get total cost test ---------------------------

def test_get_total_cost(setup_items_and_basket):
    """ Test getting total cost of basket """
    basket, tomatoSoup, *other = setup_items_and_basket
    assert basket.getTotalCost() == 12.1
    basket.addItem(tomatoSoup,5)
    assert basket.getTotalCost() == 15.6


#reset tests ---------------------------------

def test_reset(setup_items_and_basket):
    """ Test reset basket """
    #check if reset works
    basket, tomatoSoup, *other = setup_items_and_basket
    basket.reset()
    assert basket.items == {}