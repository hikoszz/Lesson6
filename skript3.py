
def xor_cipher( str, key ):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return  encript_str    
 
strg = "Реализация шифрования и дешифрования Хор"
key  = 8
print( "Оригинальная :\t", strg )
encr_strg = xor_cipher( strg, key ) 
print( "Зашифрованная :\t", encr_strg )
print( "Расшифрованная:\t", xor_cipher( encr_strg, key ) )