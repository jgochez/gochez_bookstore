# Author: Jovanny Gochez
# GitHub username: jgochez
# Date: July 5, 2023
# Description: Lemonade Stand POS Software

class InvalidSalesItemError(Exception):
    """Error function when item sold is not on menu"""
    def __init__(self, value):
        self.value = value


class MenuItem:
    """ Creates menu object with name, wholesale- and selling price"""
    def __init__(self, name, wholesale_cost, selling_price):
        ' Create data members from parameters'
        self._item_name = name
        self._wholesale_cost = wholesale_cost # float
        self._selling_price = selling_price # float
    def get_name(self):
        return self._item_name
    def get_wholesale_cost(self):
        return self._wholesale_cost # float
    def get_selling_price(self):
        return self._selling_price # float


class SalesForDay:
    """Retrieve history on sales and corresponding day"""
    def __init__(self, num_days, sales_ldictionary): # item_for_day = {item: num_sold}
        "Set up objects of how long stand has been open and its sale record"
        self._number_of_days_since_open = num_days # integer
        self._item_sold_on_specific_day = sales_ldictionary # item_for_day = {item: num_sold}

    def get_day(self):
        return self._number_of_days_since_open # integer
    def get_sales(self):
        return self._item_sold_on_specific_day # item_for_day = {item: num_sold}


class LemonadeStand:
    """Main class where program runs the menu, sales, and profit
     that will be verified, organized, and recorded"""
    def __init__(self,name):
        "Main sources of info of stand will be here including what day it is,"
        "the current menu, and current selling history"

        # Create new slate of objects to be used when menu and sales are added
        self._stand_name = name
        current_day = 0
        self._current_day = current_day
        item_and_price = {} # { item : price}
        self._menu_item_and_price = item_and_price
        sales_for_day = [] # [{day : {item : num_sold}}]
        self._sale_for_day = sales_for_day

    def get_name(self):
        return self._stand_name
    def add_menu_item(self, new_item_and_price):
        self._menu_item_and_price.update(new_item_and_price)
        return self._menu_item_and_price

    def get_price(self, name):
        for item in self._menu_item_and_price:
            if name in item:
                item_price = self._menu_item_and_price[item]

        return item_price

    def enter_sales_for_today(self, new_sale): # new_sale = {item_name : num_sold}

        try:
            # First verify sale matches menu, then we will copy our sale onto empty object
            # If the sale doesn't match menu, an error is raised
            new_dict = {}
            for new_key in new_sale:
                if new_key in self._menu_item_and_price:
                    dict = {new_key: new_sale[new_key]}
                    new_dict.update(dict)

                else:
                    raise InvalidSalesItemError(f"CAUTION: '{new_key}' was an Invalid Sale, please try again!")

            # Sale history is updated, day increased by 1
            self._sale_for_day.append(new_dict)
            self._current_day += 1
            SalesForDay(self._current_day, self._sale_for_day)

            # Main purpose is to give update of information for user
            print("current menu:", self._menu_item_and_price)
            print("current sales up to now:", self._sale_for_day)
        except InvalidSalesItemError as ise:
            print(ise)
        return self._sale_for_day

    def sales_of_menu_item_for_day(self, number_of_day, name_of_item):
        # Purpose is to find quantity of item sold on specific day
        # Call methods in SalesForDay class to extract desired information

        specific_sale = SalesForDay(self._current_day, self._sale_for_day)
        day = specific_sale.get_day()
        record = specific_sale.get_sales() # list of dict

        # Verify that day requested is valid by comparing to days since stand
        # was opened

        if number_of_day <= (day - 1):
            working_dict = record[number_of_day]
            if name_of_item in working_dict:

                return working_dict[name_of_item]

            else:
                print(f"Item '{name_of_item}' wasn't sold that day.")
        else:
            print("Stand hasn't been open for that long!")

    def total_sales_for_menu_item(self,name):
        # purpose is to find quantity of item sold there entire stand
        # has been in operation

        # Call SalesForDay class and methods to find days open and total history of sales
        specific_sale = SalesForDay(self._current_day, self._sale_for_day)
        day = specific_sale.get_day()
        record = specific_sale.get_sales()  # list of dict

        # Iterate over every day the stand has been open to find record of sales
        # If the item is found, the var quantity_count is increased by quantity of sales
        quantity_count = 0
        for i in range(0,day):
            for obj in record[i]:
                if name in obj:
                    quantity_count += (record[i][name])

        # Return quantity of sales of specific item through the entire history of stand
        return quantity_count

    def total_profit_for_menu_item(self, name):
        # Extract entire sales history and revenue based off name of item
        number_sold = self.total_sales_for_menu_item(name)
        selling_price = self.get_price(name)
        wholesale_price = selling_price / 2
        profit_for_item = number_sold * (selling_price - wholesale_price)

        # Return the profit value
        return profit_for_item

    def total_profit_for_stand(self):
        # Iterate over entire menu and return profit for each item and add them
        # onto the variable total_profit
        total_profit = 0
        for obj in self._menu_item_and_price:
            total_profit += self.total_profit_for_menu_item(obj)

        return float(total_profit)




def main():
    # Main function will call a function to add items to menu and to enter orders
    stand = LemonadeStand("I could have had a lemon?..stand")
    add_item1 = stand.add_menu_item({"strawberry": 1.00})
    add_item2 = stand.add_menu_item({"orange": 1.50})
    add_item3 = stand.add_menu_item({"hibiscus": 2.50})

    # The following three blocks of code are all three orders with
    # each having a valid and invalid order
    # The valid order go as normal and be registered
    # The invalid order will run and raise an ERROR prompting the user a message
    # Every code executed will provide print statements of how things went

    order_day_0_invalid = {"strawberry": 5, "orange": 8, "prune": 44}
    order_day_0_valid = {"strawberry": 5, "orange": 8, "hibiscus": 44}
    stand.enter_sales_for_today(order_day_0_invalid)
    stand.enter_sales_for_today(order_day_0_valid)

    order_day_1_invalid = {"strawberry": 2, "orange": 0, "prune": 3}
    order_day_1_valid = {"strawberry": 2, "orange": 0, "hibiscus": 3}
    stand.enter_sales_for_today(order_day_1_invalid)
    stand.enter_sales_for_today(order_day_1_valid)

    order_day_2_invalid = {"strawberry": 7, "orange": 50, "prune": 0}
    order_day_2_valid = {"strawberry": 7, "orange": 50, "hibiscus": 0}
    stand.enter_sales_for_today(order_day_2_invalid)
    stand.enter_sales_for_today(order_day_2_valid)

    # Check on sale of an item on a specific day
    day_n = 1
    item_search = "strawberry"
    item_sales = stand.sales_of_menu_item_for_day( day_n, item_search)
    print(f"On day '{day_n}', the number of times "
          f"the item '{item_search}' was sold was: '{item_sales}' times!")

    # The following code will return and then print total profit for item
    item_profit = stand.total_profit_for_menu_item("strawberry")
    print(f"Total profit for item was ${float(item_profit)}!")

    # The following code will execute and provide a status of total profit made by stand
    total_profit = stand.total_profit_for_stand()
    print(f"Congratulations! The total profit for the entire stand was ${float(total_profit)}!")


if __name__ == "__main__":
    main()
