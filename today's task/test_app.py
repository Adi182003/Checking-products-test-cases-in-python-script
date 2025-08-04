import unittest
from top_products import get_top_5_products

class TestTopProducts(unittest.TestCase):
    def test_top_5_output(self):
        file_path = "Data For Test.xlsx"
        result = get_top_5_products(file_path)

        expected = [
    {"Product Head": "Kettle", "Material No": 19001178, "Qty": 2749477},
    {"Product Head": "Chopper", "Material No": 19000645, "Qty": 1479910},
    {"Product Head": "Kettle", "Material No": 19001175, "Qty": 1144019},
    {"Product Head": "Kettle", "Material No": 19001177, "Qty": 1082017},
    {"Product Head": "Non-Stick Cookware", "Material No": 19000665, "Qty": 975333},
]

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
