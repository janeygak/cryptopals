from challenge_1 import hexDecode, hexEncode

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

#first hex decode
ciphertext = hexDecode(ciphertext)


def xorDecrypt(ciphertext, key):
    """Decrypts a ciphertext using the ordinal representation of a character."""
    decrypted_char = ''
    decrypted_str = ''

    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ key)
        decrypted_str += decrypted_char

    return decrypted_str


def countScore(decrypted_str):
    """Calculates the likelihood of a character being the key by counting instances of English letters (and other characters) from the decrypted text."""

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz?.,'

    score = float(0.0)
    points = float(0.0)

    for i in range(len(decrypted_str)):
        if decrypted_str[i] in letters:
            points += 1
        score = points / len(decrypted_str)
        score = score * 100

    return score


def testKeys(ciphertext):
    """Tests all possible keys and returns keys with highest likelihood of being the correct cipher key."""

    top_keys = []
    # Test against all ordinal representations

    for ord in range(0, 255, 1):
        decrypted_str = xorDecrypt(ciphertext, ord)
        score = countScore(decrypted_str)
        if score > 80:
            top_keys.append(chr(ord))

    print top_keys