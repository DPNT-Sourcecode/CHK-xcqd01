from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    def test_invalid_SKU_number(self):
        assert checkout_solution.checkout(1) == -1
    
    def test_invalid_SKU_letter(self):
        assert checkout_solution.checkout('E') == -1

    def test_valid_SKU_A(self):
        assert checkout_solution.checkout('A') == 50

    def test_valid_SKU_B(self):
        assert checkout_solution.checkout('B') == 30

    def test_valid_SKU_C(self):
        assert checkout_solution.checkout('C') == 20

    def test_valid_SKU_D(self):
        assert checkout_solution.checkout('D') == 15

    def test_valid_SKU_AB(self):
        assert checkout_solution.checkout('AB') == 80

    def test_valid_SKU_ABCDE(self):
        assert checkout_solution.checkout('ABCDA') == 165

    def test_valid_SKU_special_offer_A(self):
        assert checkout_solution.checkout('AAA') == 130

