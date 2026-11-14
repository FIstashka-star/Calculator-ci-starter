import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2.0, 3.0) == 5.0
    assert calc.add(-1.0, 1.0) == 0.0

def test_subtract(calc):
    assert calc.subtract(5.0, 3.0) == 2.0
    assert calc.subtract(1.0, 5.0) == -4.0

def test_multiply(calc):
    assert calc.multiply(3.0, 3.0) == 9.0
    assert calc.multiply(-2.0, 4.0) == -8.0

def test_divide(calc):
    assert calc.divide(10.0, 2.0) == 5.0

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5.0, 0.0)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(1.0, 3.0, 0.3333333333333333, id="one_div_three"),
        pytest.param(10.5, 2.5, 4.2, id="ten_and_half_div_two_and_half"),
        pytest.param(0.1, 0.2, 0.5, id="tenth_div_fifth"),
        pytest.param(-7.5, 2.5, -3.0, id="negative_dividend"),
        pytest.param(7.5, -2.5, -3.0, id="negative_divisor"),
        pytest.param(-7.5, -2.5, 3.0, id="both_negative"),
    ],
)
def test_divide_floats(calc, a, b, expected):
    """Проверка деления дробных чисел с учётом погрешности float."""
    result = calc.divide(a, b)
    assert result == pytest.approx(expected), (
        f"Результат деления {a} / {b} должен быть ≈ {expected}, получено {result}"
    )
