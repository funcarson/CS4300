#Task 4 test file
import pytest
from task4 import calculate_discount

#Discount method test cases
@pytest.mark.parametrize("price, discount, expected", [
    (100, 0.5, 50.0),       #integer price, float discount
    (100, 2, 200),          #integer price, integer discount
    (3.14, 0.5, 1.57),      #float price, float discount
    (100.0, 0.25, 25.0),    #float price, float discount
    (50, 0, 0),             #discount of 0 should yield 0
    (0, 0.5, 0),            #price is 0
    (-100, 0.5, -50.0),     #negative price
    (100, -0.5, -50.0),     #negative discount
])

#Method to test all test cases
def test_calculate_discount(price, discount, expected):
    result = calculate_discount(price, discount)
    if isinstance(expected, float):
        assert result == pytest.approx(expected)
    else:
        assert result == expected