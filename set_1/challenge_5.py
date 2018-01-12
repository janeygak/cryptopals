from itertools import cycle
import unittest

STANZA = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

KEY = 'ICE'

def xor_encrypt(key, plaintext):
	ciphertext = ""
	for plaintext_byte, key_byte in zip(plaintext, cycle(key)):
		xored_byte = ord(plaintext_byte) ^ ord(key_byte)
		ciphertext += chr(xored_byte)
	return ciphertext


blah = xor_encrypt(KEY, STANZA).encode('hex')

class Test(unittest.TestCase):

    def test_xor_encrypt(self):
        self.assertTrue(xor_encrypt('ICE',STANZA),'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')

if __name__ == '__main__':
    unittest.main()