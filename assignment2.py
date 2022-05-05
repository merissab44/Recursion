instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']


def find_name(names, target_name):
    output = []

    def search_for_name(index):

        if index >= len(names):
            return

        elif names[index] == target_name and len(output) == 0:
            output.append(index)

        elif names[index] != target_name and len(output) == 1:
            output.append(index - 1)

        index += 1
        search_for_name(index)

    search_for_name(0)
    return output

print(find_name(instructors, 'Braus'))