#  ============ 1.1 ============
def is_unique(s):
    if len(s) > 128:
        return False
    characters = [0] * 128
    for char in s:
        if characters[ord(char)]:
            return False
        characters[ord(char)] = True
    return True


#  ============ 1.2 ============

def get_required_letters(string):
    characters = [0] * 128
    for char in string:
        characters[ord(char)] += 1
    return characters


def check_permutation(s1, s2):
    return get_required_letters(s1) == get_required_letters(s2)


#  ============ 1.3 ============

def urlify(s, true_length):
    s, index = list(s), len(s)
    for i in reversed(range(true_length)):
        if s[i] == ' ':
            s[index - 1] = '0'
            s[index - 2] = '2'
            s[index - 3] = '%'
            index -= 3
        else:
            s[index - 1] = s[i]
            index -= 1
    return ''.join(s)


#  ============ 1.4 ============

def get_char_number(char):
    a, z, val = ord('a'), ord('z'), ord(char)
    return val - a if a <= val <= z else -1


def is_permutation_of_palindrome(phrase):
    odd_counter = 0
    table = [0] * (ord('z') - ord('a') + 1)
    for char in list(phrase):
        char_value = get_char_number(char)
        if char_value != -1:
            table[char_value] += 1
            if table[char_value] % 2 == 1:
                odd_counter += 1
            else:
                odd_counter -= 1
    return odd_counter <= 1


#  ============ 1.5 ============

def is_edit_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False
    if len(first) > len(second):
        first, second = second, first
    index1, index2 = 0, 0
    found_difference = False
    while index2 < len(second) and index1 < len(first):
        if first[index1] != second[index2]:
            if found_difference:
                return False
            else:
                found_difference = True
            if len(first) == len(second):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True


#  ============ Main ============

def main():
    print("is Unique:", is_unique("abcdefghijklmnopqrstuvwxyz"))
    print("is Permutation:", check_permutation("god", "dog"))
    print("URLify:", urlify("Mr John Smith    ", 13))
    print("is Permutation of Palindrome:", is_permutation_of_palindrome("tact coa"))
    print("is One Edit Away:", is_edit_away("pale", "ple"))


main()
