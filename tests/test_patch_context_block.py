import unittest

from unittest.mock import patch
from my_module.car import Car


def test_move_cart_is_working_successfully():
    # arrange
    car = Car()

    # act
    with patch("my_module.engine.Engine.is_enabled") as mock_method:
        mock_method.return_value = True
        response = car.move(20)

    # assert
    assert response==True
    assert car.mileage==20
