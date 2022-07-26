def vc_encrypt(message, key):
    encryption = ""
    key_chars = list(key)
    num = 0
    for i in list(message):
        spot = num % len(key_chars)
        encrypt_value = ord(i) + (ord(key_chars[spot]) - 64)
        if encrypt_value > 90:
            encrypt_value = encrypt_value - 26 # 64 is ascii of char before 'A' and there are 26 letters in the alphabet
        encryption += chr(encrypt_value)
        num += 1
    return encryption


def vc_decrypt(encrypted_message, key):
    decryption = ""
    key_chars = list(key)
    num = 0
    for i in list(encrypted_message):
        spot = num % len(key_chars)
        decrypt_value = ord(i) - (ord(key_chars[spot]) - 64)
        if decrypt_value < 65:
            decrypt_value = decrypt_value + 26 # 64 is ascii of char before 'A' and there are 26 letters in the alphabet
        decryption += chr(decrypt_value)
        num += 1
    print(decryption)
    return decryption


def run_tests():
    vc_decrypt("CSWMUCWBYHLQXRCSYQQOFQWBPSM", "INTERN") #TECHCONNECTCODINGCHALLENGES
    vc_decrypt("VVJHSMHDLHU", "CAT") #SUPERSECRET
    vc_decrypt("VQPUXBCLYCOHNXUIBNUBHITCJJAKHCQXSQCPHXYPDAGJZQCFKUSKIFQAR", "BIGBOI") #THISISACRAZYLONGMESSAGETHATISTOOLONGFORNOREASONWILLITWORK

def run_encrpyt():
    message = vc_encrypt("IAMANINTERNWORKINGHERECURRENTLYDURINGTHESUMMER", "SUMMER")
    vc_decrypt(message, "SUMMER")

if __name__ == '__main__':
    run_tests()
    run_encrpyt()
