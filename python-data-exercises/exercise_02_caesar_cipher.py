#Caesar Cipher Encode
def caesar_encode(message, offset):
  encrypted = ""
  for char in message:
    if 'a' <= char <= 'z':
      new_char = chr((ord(char) - ord('a') - offset) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
      new_char = chr((ord(char) - ord('A') - offset) % 26 + ord('A'))
    else:
      new_char = char
    encrypted += new_char
  return encrypted


#Caesar Cipher Decode
def caesar_decode(message, offset):
  decrypted = ""
  for char in message:
    if 'a' <= char <= 'z':
      new_char = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
      new_char = chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
    else:
      new_char = char
    decrypted += new_char
  return decrypted


#Caesar Cipher Test
message = 'to test encode and decode function'
offset = 6
print(caesar_encode(message,offset))
message = "ni nymn yhwixy uhx xywixy zohwncih"
print(caesar_decode(message,offset))