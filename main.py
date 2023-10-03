"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
    xvec = x.binary_vec
    yvec = y.binary_vec
    padded = pad(xvec, yvec)
    xvec = padded[0]
    yvec = padded[1]
    if (binary2int(xvec).decimal_val <= 1) and (binary2int(yvec).decimal_val <= 1):
        return BinaryNumber(binary2int(xvec).decimal_val * binary2int(yvec).decimal_val)
    else:
        x_split = split_number(xvec)
        y_split = split_number(yvec)
        x_left = x_split[0]
        x_right = x_split[1]
        y_left = y_split[0]
        y_right = y_split[1]
        xlyl = subquadratic_multiply(x_left, y_left)
        xryr = subquadratic_multiply(x_right, y_right)
        xlpxr = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
        ylpyr = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
        xlpxr_ylpyr = subquadratic_multiply(xlpxr, ylpyr)
        xlyrpxryl = BinaryNumber(xlpxr_ylpyr.decimal_val - xlyl.decimal_val - xryr.decimal_val)
        
        a = bit_shift(xlyrpxryl, len(xvec) // 2)
        b = bit_shift(xlyl, len(xvec))

        return BinaryNumber(a.decimal_val + b.decimal_val + xryr.decimal_val)
    ###


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

