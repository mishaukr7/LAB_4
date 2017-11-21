import hooke_jeeves
import unittest


class Hooke_Jeeves_test(unittest.TestCase):
    def test_precision_function(self):
        self.assertLessEqual(hooke_jeeves.image_search([3, -1, 0, 1], [1, 1, 1, 1], 1.9, 0.0001, hooke_jeeves.f), 0.001)


if __name__ == '__main__':
    unittest.main()
