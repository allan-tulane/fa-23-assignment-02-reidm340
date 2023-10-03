from main.py import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(2)) == 3*2
    assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(7)) == 5*7
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
