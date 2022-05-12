import unittest

from mock import MagicMock
from my_module.car import Car


class MagicMockTestCase(unittest.TestCase):
    def test_move_cart_is_working_successfully(self):
        # arrange
        car = Car()
        car.engine.is_enabled = MagicMock(return_value=True)

        # act
        response = car.move(20)

        # assert
        self.assertTrue(response)
        self.assertEqual(car.mileage, 20)
        car.engine.is_enabled.assert_called()
