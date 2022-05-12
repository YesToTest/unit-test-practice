import unittest

from mock import patch

from my_module.car import Car


def fake_start_engine(self):
    return True


class PatchDecoratorTestCase(unittest.TestCase):
    @patch("my_module.engine.Engine.is_enabled", fake_start_engine)
    def test_move_cart_is_working_successfully(self):
        # arrange
        car = Car()

        # act
        response = car.move(20)

        # assert
        self.assertEqual(response, True)
        self.assertEqual(car.mileage, 20)
