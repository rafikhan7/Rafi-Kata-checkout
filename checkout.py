"""checkout kata process written by Rafi"""
class Checkout:
    def __init__(self):
        """Define the price rule in a dictionary that will be accessible at the time of calculation."""
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.special_offers = {'A': {'quantity': 3, 'price': 130}, 'B': {'quantity': 2, 'price': 45}}
        self.cart = []

    def scan(self, item):
        self.cart.append(item)

    def total(self):
        """Totals function tests the price calculation against the provided test cases."""
        total_price = 0
        item_counts = {item: self.cart.count(item) for item in set(self.cart)}

        for item, count in item_counts.items():
            #This line initiates a loop that iterates over each key-value pair in the item_counts dictionary.
            #The item variable will hold the key (the item name), and the count variable will hold the corresponding value (the quantity of that item
            if item in self.special_offers:
                #This line checks if the current item has a special offer defined in the self.special_offers dictionary
                special_offer = self.special_offers[item]
                #If there is a special offer for the current item, this line retrieves the details of that special offer and assigns it to the special_offer variable.
                while count >= special_offer['quantity']:
                    #This line initiates a while loop that continues as long as the count of the current item is greater than or equal to the quantity required to avail the special offer
                    total_price += special_offer['price']
                    #Increment the total_price by the price of the special offer
                    count -= special_offer['quantity']
                total_price += count * self.prices[item]
                # Adds it to the total_price.
            else:
                total_price += count * self.prices[item]

        return total_price
        #this line returns the calculated total_price.


def price(goods):
    """Price function takes a string of goods, scans them using the Checkout object, and returns the total price."""
    co = Checkout()
    for item in goods:
        co.scan(item)
    return co.total()
