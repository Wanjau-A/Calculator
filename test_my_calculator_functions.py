from my_calculator_functions import compute_sum_of, compute_difference_of,compute_product_of,compute_division_of


def test_compute_sum_of():
    assert compute_sum_of(3, 4) == 7



def test_compute_difference_of():
    assert compute_difference_of(10, 8) == 2


def test_compute_product_of():
    assert compute_product_of(2, 10) == 20


def test_compute_division_of():
    assert compute_division_of(12, 2) == 6
