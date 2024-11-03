from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    def test_invalid_SKU(self):
        assert checkout_solution.checkout(1) == -1

