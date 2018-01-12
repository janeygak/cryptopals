def hexDecode(hex_str):
    """Converts a hex encoded string to raw bytes.

    >>> hexDecode('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    "I'm killing your brain like a poisonous mushroom"
    """

    return hex_str.decode('hex')


def hexEncode(str):
    """Converts a string to hex."""

    return str.encode('hex')


def convertToBase64(raw_bytes):
    """Converts raw bytes to base64.

    >>> convertToBase64("I'm killing your brain like a poisonous mushroom")
    'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\\n'
    """
    return raw_bytes.encode('base64')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
