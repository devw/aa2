def str2int(str):
    # The ord() function returns an integer representing the Unicode character.
    sum = 0
    for char in str:
        sum = sum + ord(char) * 6
    return sum


print(str2int("Blop"))


def get_hash(s):
    # write a function that maps a word to an integer that range from 0 to 255
    return str2int(s) % 255


print(get_hash("chien"))
print(get_hash("niche"))
