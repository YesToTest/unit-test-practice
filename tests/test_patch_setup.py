import unittest

from mock import patch
from my_module.car import Car


def fake_start_engine(self):
    return True


class PatchSetupTestCase(unittest.TestCase):
    def setUp(self):
        engine_patch = patch("my_module.engine.Engine.is_enabled", fake_start_engine)
        engine_patch.start()
        self.addCleanup(engine_patch.stop)

    def test_move_cart_is_working_successfully(self):
        # arrange
        car = Car()

        # act
        response = car.move(20)

        # assert
        self.assertTrue(response)
        self.assertEqual(car.mileage, 20)
