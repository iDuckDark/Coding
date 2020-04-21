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


#  ============ 1.6 ============

def compress(string):
    compressed = ""
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed += string[i]
            compressed += str(count_consecutive)
            count_consecutive = 0
    return compressed if len(compressed) < len(string) else string


#  ============ 1.7 ============

def rotate_matrix(matrix):
    n = len(matrix)
    if n == 0 or n != len(matrix[0]):
        return False
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
    return True


#  ============ 1.8 ============

def zero_matrix(matrix):
    row_has_zero = False
    col_has_zero = False
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            row_has_zero = True
            break
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True
            break
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    def nullify_row(row):
        for _ in range(len(matrix[0])):
            matrix[row][_] = 0

    def nullify_col(col):
        for _ in range(len(matrix)):
            matrix[_][col] = 0

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(i)
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_col(j)
    if row_has_zero:
        nullify_row(0)
    if col_has_zero:
        nullify_col(0)
    return matrix


#  ============ 1.8 ============

def is_string_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        return s2 in s1 + s1
    return False


#  ============ Main ============

def main():
    print("Is Unique:", is_unique("abcdefghijklmnopqrstuvwxyz"))
    print("Is Permutation:", check_permutation("god", "dog"))
    print("URLify:", urlify("Mr John Smith    ", 13))
    print("Is Permutation of Palindrome:",
          is_permutation_of_palindrome("tact coa"))
    print("Is One Edit Away:", is_edit_away("pale", "ple"))
    print("String Compression:", compress("aabcccccaaa"))
    matrix = [
        [5, 0, 0, 0],
        [0, 4, 0, 0],
        [0, 0, 3, 0],
        [0, 0, 0, 2],
    ]
    rotate_matrix(matrix)
    print("Matrix Rotated:", matrix)

    matrix = [
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    print("Zero Matrix:", zero_matrix(matrix))

    print("String Rotation:", is_string_rotation("waterbottle", "erbottlewat"))


main()
