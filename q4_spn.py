class SPN:
    def __init__(self):
        self.permut = {1:1, 2:5, 3:9, 4:13, 5:2, 6:6, 7:10, 8:14, 9:3,
              10:7, 11:11, 12:15, 13:4, 14:8, 15:12, 16:16}
        self.sbox = {'0000':'1110', '0001':'0100', '0010':'1101', '0011':'0001',
        '0100':'0010', '0101':'1111', '0110':'1011', '0111':'1000',
        '1000':'0011', '1001':'1010', '1010':'0110', '1011':'1100', 
        '1100':'0101', '1101':'1001', '1110':'0000', '1111':'0111'}

    def encode(self, text, key):
        assert len(key) == 32 and len(text) == 16

        subkeys = self.gen_subkeys(key)

        for r in range(len(subkeys) - 1):
            before_sbox = ''
            for i in range(len(text)):
                before_sbox += self.xor(text[i], subkeys[r][i])

            subtext = []
            for i in range(0, len(before_sbox), 4):
                subtext.append(before_sbox[i:i+4])

            after_sbox = ''
            for i in range(len(subtext)):
                subtext[i] = self.sbox[subtext[i]]
                after_sbox += subtext[i]
            
            if(r < 3):
                text = ''
                for i in range(len(after_sbox)):
                    text += after_sbox[self.permut[i+1]-1]
            
        output = ''
        for i in range(len(after_sbox)):
            output += self.xor(after_sbox[i], subkeys[4][i])

        return output

    def gen_subkeys(self, key):
        key += key
        subkeys = []
        for i in range(1, 6):
            pos = (4 * i-1) - 3
            subkeys.append(key[pos:pos+16])
        return subkeys

    def xor(self, arg1, arg2):
        return str(int(arg1) ^ int(arg2))

SPN().encode('0000000000000000', '00111010100101001101011000111111')