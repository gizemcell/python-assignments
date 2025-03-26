import sys


# to add whole column and row into impossibility which is list of excluding numbers and zeros
def add_column_row(input_lines, impossibility, row_no, colum_no):
    for row in input_lines:
        impossibility.append(row[colum_no])
    impossibility.extend(input_lines[row_no])
    return impossibility


# to determine which directions will go while looking 3*3 square
def direction(no):
    if no % 3 == 0:
        return [0, 1, 2]
    elif no % 3 == 1:
        return [-1, 0, 1]
    else:
        return [-2, -1, 0]


# adding the numbers in the 3*3 square to impossibility
def add_square(input_lines, impossibility, row_no, colum_no):
    for j in direction(row_no):
        for i in direction(colum_no):
            impossibility.append(input_lines[row_no + j][colum_no + i])
    return impossibility


# return list of possibility numbers to put cell
def decision_list(impossibilities):
    dec_list = []
    for i in range(1, 10):
        existing = "{}".format(i) in impossibilities
        if not existing:
            dec_list.append("{}".format(i))
    return dec_list


# gather all impossible numbers in a list
def emerge_impossibilities(input_lines, impossibilities, row, column):
    add_square(input_lines, impossibilities, row, column)
    add_column_row(input_lines, impossibilities, row, column)
    return impossibilities


# determine the coordinates will be filled and the value will be substituted for zero
def decision_maker(input_lines):
    begin_row, begin_column = None, None
    value = None
    for row in range(9):
        column = 0
        while column < 9 and value == None:
            temp_impossibilities = []
            if int(input_lines[row][column]) == 0:
                emerge_impossibilities(input_lines, temp_impossibilities, row, column)
                if len(decision_list(temp_impossibilities)) == 1:
                    begin_row = row
                    begin_column = column
                    value = decision_list(temp_impossibilities)[0]
            column = column + 1
    return [begin_row, begin_column, value]


# all functions are put together and be written the output file
def put_together(input_lines, output_file):
    step = 0
    while decision_maker(input_lines)[2] != None:  # until there is no value to put
        coordinates = decision_maker(input_lines)
        input_lines[coordinates[0]][coordinates[1]] = coordinates[2]
        # write last updated sudoku to outputfile
        step = step + 1
        output_file.write(18*"-"+"\n")
        output_file.write(
            "Step {} - {} @ R{}C{}\n".format(step, coordinates[2], coordinates[0] + 1, coordinates[1] + 1))
        output_file.write(18*"-"+"\n")
        row = 0
        while row < 9:
            for column in range(9):
                output_file.write(input_lines[row][column])
                if not column == 8:
                    output_file.write(" ")
                else:
                    output_file.write("\n")
            row = row + 1
    output_file.write(18*"-")


def main():
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")
    input_lines = []
    for line in input_file:
        input_lines.append(line.split())
    put_together(input_lines, output_file)
    input_file.close()
    output_file.flush()
    output_file.close()


if __name__ == "__main__":
    main()