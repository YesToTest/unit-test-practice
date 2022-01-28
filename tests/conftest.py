import pytest

from my_module.car import Car


@pytest.fixture
def car():
    return Car("Chevrolet", "Camaro", 2020)