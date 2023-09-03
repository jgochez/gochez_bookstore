from LemonadeStand import *
import unittest


class TestLemonadeStand(unittest.TestCase):

    def test_1(self):
        # Test whether name and prices appear as expected from MenuItem class
        test_name_1 = MenuItem('Testing_Testing', 11, 22)
        self.assertIs(test_name_1.get_name(), 'Testing_Testing')
        self.assertIs(test_name_1.get_wholesale_cost(), 11)
        self.assertIs(test_name_1.get_selling_price(), 22)

    def test_2(self):
        # Test whether get_sales method returns accurate number of quantity of item sold
        test_name_2 = SalesForDay(2, {"hibiscus": 4})
        self.assertEqual(test_name_2.get_day(), 2)
        self.assertEqual(test_name_2.get_sales(), {"hibiscus": 4})

    def test_3(self):
        # Test whether LemondateStand class get name method returns stand name as inputed
        test_name_3 = LemonadeStand("LemonStand INC")
        self.assertIs(test_name_3.get_name(), "LemonStand INC")

    def test_4(self):
        # Test whether enter_sales_for_today method correctly returns sale history of same day
        test_name_4 = LemonadeStand("LemonStand INC")
        add_item1 = test_name_4.add_menu_item({"strawberry": 1.00})
        add_item2 = test_name_4.add_menu_item({"orange": 1.50})
        add_item3 = test_name_4.add_menu_item({"hibiscus": 2.50})
        sale_for_day = {"strawberry": 5, "orange": 8, "hibiscus": 44}
        self.assertEqual(test_name_4.enter_sales_for_today(sale_for_day),
                         [{"strawberry": 5, "orange": 8, "hibiscus": 44}])

    def test_5(self):
        # Test whether total_sales_for_menu_item method returns entire history of item sold
        test_name_5 = LemonadeStand("LemonStand INC")
        add_item1 = test_name_5.add_menu_item({"strawberry": 1.00})
        add_item2 = test_name_5.add_menu_item({"orange": 1.50})
        add_item3 = test_name_5.add_menu_item({"hibiscus": 2.50})
        sale_for_day = {"strawberry": 5, "orange": 8, "hibiscus": 44}
        test_name_5.enter_sales_for_today(sale_for_day)
        self.assertEqual(test_name_5.total_sales_for_menu_item("strawberry"), 5)


if __name__ == '__main__':
    unittest.main()
