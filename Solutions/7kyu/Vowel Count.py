def get_count(input_str):
    num_vowels = 0
    for i in input_str:
        if i in "aeiou":
            num_vowels += 1
    return num_vowels