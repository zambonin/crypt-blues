import random
from q4_spn import SPN

sbox = {
    '0000':'1000', '0001':'0100', '0010':'0010', '0011':'0001',
    '0100':'1100', '0101':'0110', '0110':'0011', '0111':'1101',
    '1000':'1010', '1001':'0101', '1010':'1110', '1011':'0111',
    '1100':'1111', '1101':'1011', '1110':'1001', '1111':'0000',
}

key = '{0:032b}'.format(random.randint(0, 2**32))
inverse_sbox = {v: k for k, v in sbox.items()}

print(SPN().gen_subkeys(key)[4][0:4], SPN().gen_subkeys(key)[4][8:12])

def gen_pairs(k, range_):
    seq = [i for i in range(2**16)]
    random.shuffle(seq)
    pairs = []

    for i in seq[:range_]:
        i = '{0:016b}'.format(i)
        pairs += [[i, SPN().encode(i, key)]]
    return pairs

count = [[0 for i in range(16)] for j in range(16)]

for pair in gen_pairs(key, 1500):
    for i in range(16):
        for j in range(16):
            v4_1 = i ^ int(pair[1][0:4], 2)
            v4_3 = j ^ int(pair[1][8:12], 2)
            u4_1 = inverse_sbox['{0:04b}'.format(v4_1)]
            u4_3 = inverse_sbox['{0:04b}'.format(v4_3)]
            z = int(pair[0][-1]) ^ int(u4_1[0]) ^ int(u4_3[0])
            if z == 0:
                count[i][j] += 1

max_ = count[0][0]
for i in range(len(count)):
    for j in range(i):
        if count[i][j] > max_:
            max_ = count[i][j]
            pos_i = i
            pos_j = j

print('{0:04b}'.format(pos_i), '{0:04b}'.format(pos_j))