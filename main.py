import datetime
import copy


def print_board():
    for row in board:
        for square in row:
            print(square, end=' ')
        print()
    print()


def write_board_to_file():
    f = open("results.txt", "a")
    for row in board:
        for square in row:
            if square == fullSquare:
                f.write("Q")
            else:
                f.write("-")
            f.write(" ")
        f.write("\n")
    f.write("\n")
    f.close()


def set_invalidated():
    for row in range(8):
        for column in range(8):
            if board[row][column] == fullSquare:
                for x in range(8):
                    if board[x][column] != fullSquare:
                        board[x][column] = invalidSquare
                for x in range(8):
                    if board[row][x] != fullSquare:
                        board[row][x] = invalidSquare
                for x in zip(range(row, 8), range(column, 8)):
                    if board[x[0]][x[1]] != fullSquare:
                        board[x[0]][x[1]] = invalidSquare
                for x in zip(range(-row, 1), range(-column, 1)):
                    if board[-x[0]][-x[1]] != fullSquare:
                        board[-x[0]][-x[1]] = invalidSquare
                for x in zip(range(-row, 1), range(column, 8)):
                    if board[-x[0]][x[1]] != fullSquare:
                        board[-x[0]][x[1]] = invalidSquare
                for x in zip(range(row, 8), range(-column, 1)):
                    if board[x[0]][-x[1]] != fullSquare:
                        board[x[0]][-x[1]] = invalidSquare


def clear_invalidated():
    for row in range(8):
        for column in range(8):
            if board[row][column] == invalidSquare:
                board[row][column] = emptySquare


def find_next_empty():
    for row in range(8):
        for column in range(8):
            if board[row][column] == emptySquare:
                return [row, column]
    return None


def remove_last_queen():
    placedQueens[-1][2].append([placedQueens[-1][0], placedQueens[-1][1]])
    board[placedQueens[-1][0]][placedQueens[-1][1]] = emptySquare
    clear_invalidated()
    set_invalidated()
    for coords in placedQueens[-1][2]:
        board[coords[0]][coords[1]] = invalidSquare
    remainingEmptySquares = True
    for row in range(8):
        for column in range(8):
            if board[row][column] == emptySquare:
                remainingEmptySquares = False
    if remainingEmptySquares:
        placedQueens.pop()
        remove_last_queen()


def place_queen():
    coords = find_next_empty()
    if coords != None:
        board[coords[0]][coords[1]] = fullSquare
        set_invalidated()
        placedCount = 0
        for row in range(8):
            for column in range(8):
                if board[row][column] == fullSquare:
                    placedCount += 1
        if placedCount == len(placedQueens) + 1:
            placedQueens.append([coords[0], coords[1], []])
        else:
            placedQueens[-1][0] = coords[0]
            placedQueens[-1][1] = coords[1]
    else:
        remove_last_queen()


def add_transforms():
    boardCopy = copy.deepcopy(board)
    boardCopy.reverse()
    configuration.append(boardCopy)
    boardCopy = copy.deepcopy(board)
    for x in range(8):
        boardCopy[x].reverse()
    configuration.append(boardCopy)
    boardCopy = copy.deepcopy(board)
    for x in range(8):
        boardCopy.reverse()
    boardCopy.reverse()
    configuration.append(boardCopy)
    boardCopy = copy.deepcopy(board)
    for row in range(8):
        for column in range(8):
            boardCopy[column][row] = board[row][column]
    configuration.append(boardCopy)
    boardCopy = copy.deepcopy(board)
    for row in range(8):
        for column in range(8):
            boardCopy[column][row] = board[row][column]
    for x in range(8):
        boardCopy[x].reverse()
    configuration.append(boardCopy)
    boardCopy = copy.deepcopy(board)
    for row in range(8):
        for column in range(8):
            boardCopy[column][row] = board[row][column]
    boardCopy.reverse()
    configuration.append(boardCopy)
    boardCopy = copy.deepcopy(board)
    for row in range(8):
        for column in range(8):
            boardCopy[column][row] = board[row][column]
    boardCopy.reverse()
    for x in range(8):
        boardCopy[x].reverse()
    configuration.append(boardCopy)


def find_configuration():
    while True:
        place_queen()
        if len(placedQueens) == 8:
            if 0 == len(configuration):
                configuration.append(board)
                add_transforms()
                print_board()
                return
            newBoard = True
            for x in configuration:
                if list(board) == x:
                    newBoard = False
            if newBoard:
                configuration.append(board)
                add_transforms()
                print_board()
                return
            remove_last_queen()


emptySquare = 8
fullSquare = 1
invalidSquare = 0
configuration = []

f = open("results.txt", "w")
f.close()

overallStartTime = datetime.datetime.now()

for x in range(12):
    startTime = datetime.datetime.now()
    print("Starting board:", x+1, "\nStart timestamp:", startTime)
    board = [[emptySquare for x in range(8)] for x in range(8)]
    placedQueens = []
    find_configuration()
    endTime = datetime.datetime.now()
    print("Time taken to find board:", endTime - startTime, "\n")
    f = open("results.txt", "a")
    f.write(" ".join(["Time taken to find board", str(x + 1), ":", str(endTime - startTime), "\n"]))
    f.close()
    write_board_to_file()

overallTime = datetime.datetime.now() - overallStartTime
print("Overall time:", overallTime)
f = open("results.txt", "a")
f.write(" ".join(["Overall time:", str(overallTime)]))
f.close()
