import unittest

from mock import patch
from my_module.car import Car


class PatchContextBlockTestCase(unittest.TestCase):
    def test_move_cart_is_working_successfully(self):
        # arrange
        car = Car()

        # act
        with patch("my_module.engine.Engine.is_enabled") as mock_method:
            mock_method.return_value = True
            response = car.move(20)

        # assert
        self.assertTrue(response)
        self.assertEqual(car.mileage, 20)
