instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']


def find_name(names, target_name):
    output = []
    def search_for_name(index):

        if index >= len(names):
            return

        elif names[index] == target_name and len(output) == 0:
            output.append(index)
            if names[index + 1] != target_name:
                return output

        elif names[index] != target_name and len(output) == 1:
            output.append(index - 1)

        search_for_name(index + 1)

    search_for_name(0)
    return output

print(find_name(instructors, 'Braus'))

# problem 2
result = []
digits = {"2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "qprs",
          "8": "tuv",
          "9": "wxyz", }


def letter_combonations(index, currentString):
    if len(currentString) == len(digits):
        result.append(currentString)
        return

    for char in digits[currentString[index]]:
        print(char)
        letter_combonations(index + 1, currentString + char)


letter_combonations(0, "34")
print(result)