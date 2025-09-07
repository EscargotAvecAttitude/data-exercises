# Vigenère Cipher Encode
def vigenere_encrypt(message, keyword):
    encrypted = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in message:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            shift = ord(keyword[keyword_index % keyword_length]) - ord('a')

            if 'a' <= char <= 'z':
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            encrypted += new_char
            keyword_index += 1
        else:
            encrypted += char
    return encrypted


# Vigenère Cipher Decode
def vigenere_decrypt(message, keyword):
    decrypted = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in message:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            shift = ord(keyword[keyword_index % keyword_length]) - ord('a')

            if 'a' <= char <= 'z':
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            decrypted += new_char
            keyword_index += 1
        else:
            decrypted += char
    return decrypted

#Vigenère Cipher Test
message = 'to test encode and decode function'
keyword = 'friends'
print(vigenere_encrypt(message,keyword))
message = 'ox lafq milgzr xvy mwybam adfygfwi'
print(vigenere_decrypt(message,keyword))