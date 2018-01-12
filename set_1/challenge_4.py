from challenge_3 import xorDecrypt, countScore, testKeys
from challenge_1 import hexDecode

file = open("4.txt").read().split()

def search_file(file):
	for line in file:
		for key in range(0,256): #iterate 0-255 ord nums as key
			decrypted_line = xorDecrypt(hexDecode(line), key) #decrypt line with key
			score = countScore(decrypted_line) #check likelihood of decrypted line
			if score > 80:
				print decrypted_line, score
			key = key + 1



