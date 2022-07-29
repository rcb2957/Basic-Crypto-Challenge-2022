
def cc_encrypt(message, key):
    encryption = ""
    key = abs(key) % 26
    for i in list(message):
        encrypt_value = ord(i) + key
        if encrypt_value > 90:
            encrypt_value = encrypt_value - 26 # 64 is ascii of char before 'A' and 90 is ascii value of 'Z' and 90 - 64 = 26
        encryption += chr(encrypt_value)
    print(encryption)
    return encryption


def cc_decrypt(decrypted_message, key):
    decryption = ""
    key = abs(key) % 26
    for i in list(decrypted_message):
        decrypt_value = ord(i) - key
        if decrypt_value < 65:
            decrypt_value = decrypt_value + 26 # 64 is ascii of char before 'A' and there are 26 letters in the alphabet
        decryption += chr(decrypt_value)
    print(decryption)
    return decryption


def run_tests():
    cc_decrypt("ALZAPUN", 7)  #TESTING
    cc_decrypt("JXKAQYXKH", 23) #MANDTBANK
    cc_decrypt("BSUOHWJS", -14) #NEGATIVE
    cc_decrypt("HUQBBOBEDWJUNJMYJXRYWDKCRUH", 135762) #REALLYLONGTEXTWITHBIGNUMBER

def run_encrpyt():
    message = cc_encrypt("IWORKINSENECAONEBUTSOMETIMESTHELARKINBUILDING", 465)
    cc_decrypt(message, 465)

if __name__ == '__main__':
    run_tests()
    run_encrpyt()
