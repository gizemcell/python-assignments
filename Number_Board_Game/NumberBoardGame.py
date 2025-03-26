import sys


#calculation the lenght of row and column
def row_column_len(input_lines):
    if len(input_lines) == 0:
        return [0, 0]
    else:
        return [len(input_lines), len(input_lines[0])]


#find direction to search neighbours relating to index of row
def find_direction_row(input_lines, row):
    if row_column_len(input_lines)[0] == 1:
        return [0]
    elif row == row_column_len(input_lines)[0]-1:
        return [-1, 0]
    elif row == 0:
        return [0, 1]
    else:
        return [-1, 0, 1]


#find direction to search neighbours relating to index of column
def find_direction_column(input_lines, column):
    if row_column_len(input_lines)[1] == 1:
        return [0]
    elif column == row_column_len(input_lines)[1] - 1:
        return [-1, 0]
    elif column == 0:
        return [0, 1]
    else:
        return [-1, 0, 1]


#searching neighbours have same value with the selected index by user, then adding them index list
#index list consists of all neighbours have equal value and then later to use for searching again
# if neighbour's neighbours have same value
def finding_neighbours(input_lines, row, column, index):
    if input_lines[row][column] != " ":
        for row2 in find_direction_row(input_lines,row):
            if input_lines[row][column] == input_lines[row + row2][column]:
                for column2 in find_direction_column(input_lines,column):
                    if input_lines[row][column] == input_lines[row+row2][column+column2]:
                        if not [row+row2,column+column2] in index:
                            index.append([row+row2, column+column2])
    return index


#every time index list will be expanded until there is no neighbour has equal value
def recursion(input_lines, row, column, index):
    finding_neighbours(input_lines, row, column, index)
    if index != []:
        for i in index:
            finding_neighbours(input_lines, i[0], i[1], index)
        return index
    else:
        return index


#the neighbours will be deleted changes them value to space
def deleting_places(index, input_lines):
    for i in index:
        input_lines[i[0]][i[1]] = " "


#if there is a number above a space then their places are swapped each other
def sliding(input_lines):
    lenghts = row_column_len(input_lines)
    for row in range(lenghts[0]):
        for column in range(lenghts[1]):
            row2=row
            if input_lines[row2][column] == " ":
                while input_lines[row2-1][column] != " " and row2 < lenghts[0] and 0 <= row2-1:
                    (input_lines[row2][column], input_lines[row2-1][column]) = (input_lines[row2-1][column], input_lines[row2][column])
                    row2 = row2-1


#deleting whole empty row
def delete_empty_row(input_lines):
    lenghts = row_column_len(input_lines)
    while True:
        control2 = True #controlling if there is a empty row otherwise while loop will be stopped
        lenghts = row_column_len(input_lines)
        for row in range(lenghts[0]):
            control = True #controllng if the cell is a space or not
            for column in range(lenghts[1]):
                if input_lines[row][column] != " ":
                    control = False
                    break
            if control:
                input_lines.pop(row)
                control2 = False  # it means there is empty row then look again presence of empty row
                break
        if control2:
            break
    return input_lines


#deleting empty column by using same approach with deleting empty row
def delete_empty_column(input_lines):
    lenghts = row_column_len(input_lines)
    while True:
        control2 = True
        lenghts = row_column_len(input_lines)
        for column in range(lenghts[1]):
            control = True
            for row in range(lenghts[0]):
                if input_lines[row][column] != " ":
                    control = False
                    break
            if control:
                for row2 in range(lenghts[0]):
                    input_lines[row2].pop(column)
                control2 = False
                break
        if control2:
            break


def score(destroyed_number, value):
    return destroyed_number*value


#puuting all pieces together
def play_game(input_lines, row, column):
        index = []
        recursion(input_lines, row, column, index)
        deleting_places(index, input_lines)
        sliding(input_lines)
        delete_empty_row(input_lines)
        delete_empty_column(input_lines)
        return index


#returning false means game is over otherwise game must be continue
#temp_index is used for to add neighbours if there is otherwise it will be empty or just one cell is selected cell
def game_over(input_lines):
    lenghts = row_column_len(input_lines)
    temp_index = []
    for row in range(lenghts[0]):
        for column in range(lenghts[1]):
            temp_index = []
            finding_neighbours(input_lines, row, column, temp_index)
            if len(temp_index) > 1:
                return True
    return False


def printing(input_lines):
    for line in input_lines:
        for item in line:
            print(item, end=" ")
        print()


def main():
    input_file = open(sys.argv[1], "r")
    input_lines = []
    for line in input_file:
        input_lines.append(line.split())
    input_file.close()
    grade = 0
    while True:
        printing(input_lines)
        print("\nYour score is: ", grade)
        if game_over(input_lines) == False:
            print("\nGame over")
            break
        coordinates = input("\nPlease enter a row and column number: ").split()
        print()
        row = int(coordinates[0])-1
        column = int(coordinates[1])-1
        temp_list = []
        if row < 0 or row > row_column_len(input_lines)[0] or column < 0 or column > row_column_len(input_lines)[1]:
            print("Please enter a correct size!\n")
        elif len(finding_neighbours(input_lines, row, column, temp_list)) < 2:
            print("No movement happened try again\n")
        else:
            value = int(input_lines[row][column])
            grade = grade + score(len(play_game(input_lines, row, column)), value)


if __name__ == "__main__":
    main()