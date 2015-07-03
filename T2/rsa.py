import pollard
import utils

def decode26(enc_num):
    coefficients = []
    while enc_num:
        coefficients.append(enc_num % 26)
        enc_num //= 26
    
    still_enc = ""
    for num in coefficients[::-1]:
        still_enc += chr(num + 65)

    return still_enc

def phi(n):
    p = pollard.factor(n)
    return (p-1)*((n/p)-1)

def rsa_dec(text=enc_text, n=31313, b=4913):
    final_text = ""
    a = utils.inv_mod(b, phi(n))
    for i in text:
        final_text += decode26(utils.quad_mult(i, a, n))
    return final_text