import unittest

from mock import MagicMock

from my_module.car import Car


class MagicMockTestCase(unittest.TestCase):

    def test_is_engine_working_calling_right(self):
        # arrange
        car = Car("Chevrolet", "Camaro", 2020)
        car.engine.start_engine = MagicMock(return_value=True)

        # act
        response = car.is_engine_working()

        # assert
        self.assertTrue(response)
        car.engine.start_engine.assert_called()

    def test_engine_is_not_working(self):
        # arrange
        car = Car("Mazda", "CX5", 2021)
        car.engine.start_engine = MagicMock(return_value=False)

        # act
        response = car.is_engine_working()

        # assert
        self.assertFalse(response)
        car.engine.start_engine.assert_called()
