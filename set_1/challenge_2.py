from challenge_1 import hexDecode, hexEncode
import unittest

def areEqualLen(a,b):
    """Checks if two buffers are equal length."""

    if len(a) != len(b):
        return False
    else:
        return True


def fixedXor(a,b):
    xor = ''
    result = ''

    for pair in zip(a, b):
        xor = ord(pair[0]) ^ ord(pair[1])
        bit = chr(xor)
        result += bit

    return result


def doFixedXor(a,b):
    if not areEqualLen(a,b):
        return("Error. Must be equal length buffers.")
    else:
        # First decode from hex
        a = hexDecode(a)
        b = hexDecode(b)

        xor = fixedXor(a,b)
        return xor

# Test buffers
a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'



class Test(unittest.TestCase):

    def test_areEqualLen(self):
        self.assertTrue(areEqualLen('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'), True)

    def test_doFixedXor(self):
        self.assertEqual(doFixedXor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'),'the kid don\'t play')

    def test_doFixedXor_hex_encode(self):
        self.assertEqual(hexEncode(doFixedXor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')),'746865206b696420646f6e277420706c6179')


if __name__ == '__main__':
    unittest.main()