import random
from q4_spn import SPN

bits = ["{0:0>4}".format(bin(i)[2:]) for i in range(16)]
key = '00111010100101001101011000111111'

def gen_quadruples(chosen_xor='1011'):
	tuples = []
	for i in bits:
		u = ''
		for j in range(4):
			u += SPN().xor(chosen_xor[j], i[j])
		tuples += [(i, u, SPN().sbox[i], SPN().sbox[u])]

	quadruples = []
	for each in tuples:
		for i in range(16):
			for j in range(4):
				bits1 = bits[i] + each[0] + '1001' + bits[j]
				bits2 = bits[i] + each[1] + '1001' + bits[j]
				quadruples.append((bits1, bits2, SPN().encode(bits1, key), SPN().encode(bits2, key)))

	return random.sample(quadruples, 200)

def multi_xor(arg1, arg2):
	xor = ''
	for i in range(len(arg1)):
		xor += SPN().xor(arg1[i], arg2[i])
	return xor

def diff_attack(quadruples=gen_quadruples()):
	inverse_sbox = {v: k for k, v in SPN().sbox.items()}

	tentatives = []
	for i in range(16):
		for j in range(16):
			tentatives.append([bits[i], bits[j]])

	count = [0] * len(tentatives)

	for each in quadruples:
		if each[2][0:4] == each[3][0:4] and each[2][8:12] == each[3][8:12]:
			for key in tentatives:		
				v2 = multi_xor(key[0], each[2][4:8])
				v4 = multi_xor(key[1], each[2][12:16])
				v2_star = multi_xor(key[0], each[3][4:8])
				v4_star = multi_xor(key[1], each[3][12:16])
				
				u2 = inverse_sbox[v2]
				u4 = inverse_sbox[v4]
				u2_star = inverse_sbox[v2_star]
				u4_star = inverse_sbox[v4_star]

				u2_line = multi_xor(u2, u2_star)
				u4_line = multi_xor(u4, u4_star)

				if u2_line == '0110' and u4_line == '0110':
					count[tentatives.index(key)] += 1
	
	return tentatives[count.index(max(count))]

assert diff_attack() == ['0110', '1111']