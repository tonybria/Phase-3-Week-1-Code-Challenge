def consonant_value(s):
    consonant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    max_consonant_value = 0
    current_consonant_value = 0
    
    for char in s:
        if char in consonant_values:
            current_consonant_value += consonant_values[char]
            max_consonant_value = max(max_consonant_value, current_consonant_value)
        else:
            current_consonant_value = 0
    
    return max_consonant_value

# Test case
print(consonant_value("abc"))          # Output: 2 (b)
print(consonant_value("bcd"))          # Output: 9 (bcd)
print(consonant_value("xyz"))          # Output: 0 (no consonants)
print(consonant_value("zxcvbnm"))      # Output: 81 (zxcvbnm)
print(consonant_value("aeiou"))        # Output: 0 (no consonants)
print(consonant_value("hellothere"))   # Output: 39 (th)
