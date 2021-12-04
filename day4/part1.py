def check_horizontal(marked_board):
    for row in marked_board:
        row_count = 0
        for item in row:
            if item == False:
                row_count = 0
                break
            row_count += 1
            if row_count == 5:
                return True
    return False
        
def check_vertical(marked_board):
    for column in range(len(marked_board)):
        column_count = 0
        for row in range(len(marked_board)):
            if marked_board[row][column] == False:
                column_count = 0
                break
            column_count += 1
            if column_count == 5:
                return True
    return False

def check_for_bingo(marked_board):
    if check_horizontal(marked_board) or check_vertical(marked_board):
        return True
    return False

def play_bingo(drawn_numbers, boards):
    is_first = True
    min_bingo_rounds = 0
    winning_conditions = ()
    for board in boards:
        round_count = 0
        marked_board = [[False for j in range(len(board))] for i in range(len(board))]
        for number in drawn_numbers:
            round_count += 1
            for row in range(len(board)):
                for column in range(len(board)):
                    if board[row][column] == number:
                        marked_board[row][column] = True
            if check_for_bingo(marked_board):
                if is_first or round_count < min_bingo_rounds:
                    winning_conditions = (board, marked_board, number)
                    min_bingo_rounds = round_count
                    is_first = False
                    break
                            
    return winning_conditions
                
def calculate_score(board, marked_board, winning_number):
    total = 0
    for row in range(len(board)):
        for column in range(len(board)):
            if marked_board[row][column] == False:
                total += board[row][column]
    return total * winning_number

def read_bingo_game(file):
    drawn_numbers = []
    boards = []

    with open(file) as f:
        is_first = True
        cur_board = []
        for line in f:
            if is_first:
                drawn_numbers = list(map(int, line.split(",")))
                is_first = False
                continue
            if line == "\n":
                cur_board = []
                board_row_count = 0
            else:
                cur_board.append(list(map(int, line.split())))
                board_row_count += 1
            if board_row_count == 5:
                boards.append(cur_board)
    
    return drawn_numbers, boards

winning_conditions = play_bingo(*read_bingo_game("input.txt"))
print(calculate_score(*winning_conditions))

