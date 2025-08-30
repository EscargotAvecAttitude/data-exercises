def caesar_decode(message, offset):
    spread_char = list(message)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_spread_char = []
    for char in spread_char:
        if char in alphabet:
            new_char = alphabet[alphabet.index(char) + offset]
        else:
            new_char = char
        new_spread_char.append(new_char)
    return (''.join(new_spread_char))


def caesar_encode(message, offset):
    spread_char = list(message)
    alphabet = ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_spread_char = []
    for char in spread_char:
        if char in alphabet:
            new_char = alphabet[alphabet.index(char) - offset]
        else:
            new_char = char
        new_spread_char.append(new_char)
    return (''.join(new_spread_char))

message = "xubbe!"
offset = 10
print(caesar_decode(message, offset))

message = "goodbye!"
offset = 14
print(caesar_encode(message, offset))