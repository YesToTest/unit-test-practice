import unittest

from mock import patch

from my_module.car import Car


class PatchContextBlockTestCase(unittest.TestCase):

    def test_is_engine_working_successfully(self):
        # arrange
        car = Car("Chevrolet", "Sail", 2018)

        # act
        with patch("my_module.engine.Engine.start_engine") as mock_method:
            mock_method.return_value = True
            response = car.is_engine_working()

        # assert
        self.assertEqual(response, True)
