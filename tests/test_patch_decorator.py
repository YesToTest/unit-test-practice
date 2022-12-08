import unittest
from unittest.mock import patch

from my_module.car import Car


def fake_is_enabled(self):
    return True


class PatchDecoratorTestCase(unittest.TestCase):
    @patch("my_module.engine.Engine.is_enabled", fake_is_enabled)
    def test_move_cart_is_working_successfully(self):
        # arrange
        car = Car()

        # act
        response = car.move(20)

        # assert
        self.assertEqual(response, True)
        self.assertEqual(car.mileage, 20)
