import unittest

from unittest.mock import MagicMock
from my_module.car import Car


def test_move_cart_is_working_successfully():
    # arrange
    car = Car()
    car.engine.is_enabled = MagicMock(return_value=True)

    # act
    response = car.move(20)

    # assert
    assert response==True
    assert car.mileage==20
    car.engine.is_enabled.assert_called()
