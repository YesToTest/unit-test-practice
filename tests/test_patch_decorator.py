import unittest

from mock import patch

from my_module.car import Car


def fake_start_engine(self):
    return True


class PatchDecoratorTestCase(unittest.TestCase):

    @patch("my_module.engine.Engine.start_engine", fake_start_engine)
    def test_is_engine_working_successfully(self):
        # arrange
        car = Car("Chevrolet", "Sail", 2018)

        # act
        response = car.is_engine_working()

        # assert
        self.assertEqual(response, True)

    @patch("my_module.engine.Engine.start_engine", lambda _: True)
    def test_is_moving_successfully(self):
        # arrange
        car = Car("Chevrolet", "Sail", 2018)
        distance = 20

        # act
        response = car.move_distance(distance)

        # assert
        self.assertEqual(response, distance)
