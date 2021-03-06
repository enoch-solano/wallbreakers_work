"""

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!

# isToeplitz

# [[1]] -> true

# 1 3 6 4
# 2 1 3 6
# 5 2 1 3 -> true

# 1   3  6  4
# 2 1 - 1 6
# 5 2 1  3 -> false

# 4 6 3 1
# 6 3 1 2 -> false

# [[1, 2, 4, 5, 6]] -> true

# number of columns not equal to rows
[
    [1],
    [2, 3],
    [3, 4, 6],
]
"""


def isToeplitz(matrix):  # O(n * m)
    if not matrix:
        return True
    rows_length = len(matrix)

    for i in range(1, rows_length):  # O(n)
        for j in range(1, matrix[i]):  # O(m)
            # compare to the top left neighbor
            if matrix[i][j] != matrix[i-1][j-1]:
                return False
    return True

#     rows = len(matrix)  # n
#     cols = len(matrix[0])  # m

#     for col in range(cols - 1):  # check first row
#         if not check_diagonal(matrix, 0, col):
#             return False  # O(1)

#     # we already check the first index of the row's index so start at 1
#     for row in range(1, rows - 1):
#         # we do not need to check the last row of the rows because it will be alone it it being single is true in itself.
#         if not check_diagonal(matrix, row, 0):
#             return False

#     return True


# def check_diagonal(matrix, i, j):  # bool
#     constant = matrix[i][j]
#     i += 1
#     j += 1
#     rows = len(matrix)
#     cols = len(matrix[0])

#     while i < rows and j < cols:
#         if matrix[i][j] != constant:
#             return False
#         i += 1
#         j += 1

#     return True


# "theweatherisnice" -> "the weather is nice"
# "t h e w e a" -> ""


def _is_in_dictionary(substring):  # true or false
    pass


def turn_string_words(s):
    result = []
    word = ""

    for char in s:  # O(n)

        if _is_in_dictionary(word):
            result.append(word)  # O(1)
            word = ""  # O(1)

        word += char  # O(n)

    # last check for the word ...
    if _is_in_dictionary(word):
        result.append(word)
        word = ""

    if word:  # if there is still characters
        return ""

    sentence = " ".join(result)  # O(n)
    return sentence.strip()  # O(n)
