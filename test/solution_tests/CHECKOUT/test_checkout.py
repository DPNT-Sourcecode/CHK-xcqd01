from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    def test_invalid_SKU_number(self):
        assert checkout_solution.checkout(1) == -1

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

    def test_valid_SKU_special_offer_B(self):
        assert checkout_solution.checkout('BB') == 45

    def test_complex_SKU_entry(self):
        assert checkout_solution.checkout('ABCDABCD') == 215

    def test_valid_SKU_E(self):
        assert checkout_solution.checkout('E') == 40

    def test_valid_SKU_EE(self):
        assert checkout_solution.checkout('EE') == 80

    def test_valid_SKU_EEB(self):
        assert checkout_solution.checkout('EEB') == 80

    def test_valid_SKU_special_offer_AAAAA(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_valid_SKU_special_offer_BEBEEE(self):
        assert checkout_solution.checkout('BEBEEE') == 160

    def test_complex_SKU_entry_ABCDEABCDE(self):
        assert checkout_solution.checkout('ABCDEABCDE') == 280

    def test_valid_SKU_special_offer_FFF(self):
        assert checkout_solution.checkout('FFF') == 20

    def test_valid_SKU_special_offer_FFFF(self):
        assert checkout_solution.checkout('FFFF') == 30

    def test_valid_SKU_special_offer_FFFFF(self):
        assert checkout_solution.checkout('FFFFF') == 40

    def test_complex_SKU_entry_FFFFEEBADEF(self):
        assert checkout_solution.checkout('FFFFEEBADEF') == 225

    def test_valid_SKU_special_offer_5H(self):
        assert checkout_solution.checkout('HHHHH') == 45

    def test_valid_SKU_special_offer_10H(self):
        assert checkout_solution.checkout('HHHHHHHHHH') == 80

    def test_valid_SKU_special_offer_2K(self):
        assert checkout_solution.checkout('KK') == 120  # Updated to reflect the new price

    def test_valid_SKU_special_offer_3N(self):
        assert checkout_solution.checkout('NNNMM') == 135

    def test_valid_SKU_special_offer_5P(self):
        assert checkout_solution.checkout('PPPPP') == 200

    def test_valid_SKU_special_offer_3Q(self):
        assert checkout_solution.checkout('QQQ') == 80

    def test_valid_SKU_special_offer_3R(self):
        assert checkout_solution.checkout('RRRQ') == 150

    def test_valid_SKU_special_offer_4U(self):
        assert checkout_solution.checkout('UUUU') == 120

    def test_complex_SKU_entry_ABXZRRRQQQ(self):
        assert checkout_solution.checkout('ABXZRRRQQQ') == 328

    def test_valid_SKU_many_Hs(self):
        assert checkout_solution.checkout('HHHHHHHHHHHHHHH') == 125

    def test_special_offer_SSS(self):
        assert checkout_solution.checkout('SSS') == 45

    def test_special_offer_TTT(self):
        assert checkout_solution.checkout('TTT') == 45

    def test_special_offer_XXX(self):
        assert checkout_solution.checkout('XXX') == 45

    def test_special_offer_YYY(self):
        assert checkout_solution.checkout('YYY') == 45

    def test_special_offer_ZZZ(self):
        assert checkout_solution.checkout('ZZZ') == 45

    def test_special_offer_SSSSSS(self):
        assert checkout_solution.checkout('SSSSSS') == 90 

    def test_special_offer_TTTTTTTTTT(self):
        assert checkout_solution.checkout('TTTTTTTTTT') == 155 

    def test_special_offer_SSSS(self):
        assert checkout_solution.checkout('SSSS') == 65  

    def test_special_offer_TTTT(self):
        assert checkout_solution.checkout('TTTT') == 65  

    def test_special_offer_XXXYYY(self):
        assert checkout_solution.checkout('XXXYYY') == 90

    def test_special_offer_STX(self):
        assert checkout_solution.checkout('STX') == 45

    def test_special_offer_STXSTX(self):
        assert checkout_solution.checkout('STXSTX') == 90

    def test_special_offer_SSSZ(self):
        assert checkout_solution.checkout('SSSZ') == 66



