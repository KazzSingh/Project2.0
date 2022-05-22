
import config as cnfg
import main
import products as pm
import couriers as cm
import orders as om
import test_area as tst
import unittest

product_list = []
courier_list = []
order_list = []

main_menu = ["Exit", "Product Menu Options",
             "Courier Menu Options", "Order Menu Options"]

product_menu = ["Return to Main Menu", "Product List", "Create new Product!",
                "Update existing Product!", "Delete Product"]


# ###########################################################################################
# pm
class TestCreate(unittest.TestCase):

    # def test_product_name(self):
    #     self.assertEqual(tst.product_name("banana"), "banana")
    #     self.assertEqual(tst.product_name("0"), "pm.run_product_sequence")
    #     self.assertEqual(tst.product_name("389749"),
    #                      "(\n Please enter a valid product name) product_name()")

    # ###########################################################################################

    def test_product_price(self):
        self.assertEqual(tst.product_price("0.99"), '')
        self.assertEqual(tst.product_price('.99'), '0.99')
        self.assertEqual(tst.product_price("9.99"), '9.99')
        self.assertEqual(tst.product_price("9"), '9.00')
        self.assertEqual(tst.product_price("nine"), "not valid")
        self.assertEqual(tst.product_price("X"), "run_product_sequence()")
        self.assertEqual(tst.product_price("x"), "run_product_sequence()")

        ################################################################
# pm


if __name__ == '__main__':
    unittest.main()
