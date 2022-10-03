import random
from time import sleep


class TicTacToe:

    # INITIALIZE BOARD
    def __init__(self):
        self.board = []

    # CREATE BOARD
    def create_board(self):
        # FOR LOOP - EACH ROW
        for i in range(3):
            # CREATE EMPTY ROW
            row = []
            # FOR LOOP - EACH COLUMN
            for j in range(3):
                # ADD DASH TO EACH COLUMN FOR THE CURRENT ROW
                row.append('-')
            # COMPLETE BOARD
            self.board.append(row)

    # SELECT FIRST PLAYER AT RANDOM
    def get_random_first_player(self):
        return random.randint(0, 1)

    # ASSOCIATE SPOT WITH PLAYER
    def fix_spot(self, row, col, player):
        # IF THE CHOSEN SPOT IS EMPTY
        if self.board[row][col] == "-":
            # ASSOCIATE SPOT WITH GIVEN PLAYER
            self.board[row][col] = player
            # RETURN TRUE
            return True
        # IF THE CHOSEN SPOT HAS ALREADY BEEN TAKEN
        else:
            # INFORM USER OF TAKEN SPOT
            print(f"The chosen spot is invalid, please try again.")
            # RETURN FALSE
            return False

    # CHECK IF PLAYER HAS WON
    def is_player_win(self, player):

        # INITIALIZE WIN VARIABLE
        win = None

        # OBTAIN LENGTH OF BOARD (3)
        n = len(self.board)

        # CHECK EACH ROW
        for i in range(n):
            # SET WIN VARIABLE TO TRUE
            win = True
            # CHECK EACH POSITION IN THE ROW
            for j in range(n):
                # IF CURRENT POSITION IS NOT ASSOCIATED WITH A PLAYER
                if self.board[i][j] != player:
                    win = False
                    break
            # AFTER CHECKING CURRENT ROW | IF WIN = TRUE | RETURN WIN
            if win:
                return win

        # CHECK EACH COLUMN
        for i in range(n):
            # INITIALIZE WIN VARIABLE
            win = True
            # CHECK EACH POSITION IN THE COLUMN
            for j in range(n):
                # IF THE CURRENT POSITION IN NOT ASSOCIATE WITH CURRENT PLAYER
                if self.board[j][i] != player:
                    win = False
                    break
            # AFTER CHECKING CURRENT COLUMN | IF WIN = TRUE | RETURN WIN
            if win:
                return win

        # INITIALIZE WIN VARIABLE
        win = True
        # CHECK DIAGONALS
        for i in range(n):
            # IF ANY OF THE DIAGONAL POSITIONS != CURRENT PLAYER WIN = FALSE
            if self.board[i][i] != player:
                win = False
                break
        # AFTER CHECKING CURRENT DIAGONAL | IF WIN = TRUE | RETURN WIN
        if win:
            return win
        # INITIALIZE WIN VARIABLE
        win = True
        # CHECK BACKWARDS DIAGONAL
        for i in range(n):
            # IF ANY OF THE DIAGONAL POSITIONS != CURRENT PLAYER WIN = FALSE
            if self.board[i][n-1-i] != player:
                win = False
                break
        # AFTER CHECKING CURRENT DIAGONAL | IF WIN = TRUE | RETURN WIN
        if win:
            return win
        # OTHERWISE RETURN FALSE
        return False

    # CHECK IF BOARD IS FILLED
    def is_board_filled(self):
        # LOOP THROUGH EACH ROW
        for row in self.board:
            # LOOP THROUGH EACH ITEM IN THE CURRENT ROW
            for item in row:
                # CHECK IF ITEM IS EMPTY | RETURN FALSE
                if item == "-":
                    return False
        # RETURN TRUE OTHERWISE
        return True

    # SWAP PLAYER TURN
    def swap_player_turn(self, player):
        return 'X' if player == "O" else "O"

    # SHOW BOARD
    def show_board(self):
        # LOOP THROUGH EACH ROW
        for row in self.board:
            # LOOP THROUGH EACH ITEM IN ROW
            for item in row:
                # PRINT EACH ITEM WITH A SPACE AFTER
                print(item, end=" ")
            print()

    # START GAME
    def start(self):
        # PRINT WELCOME
        print("Welcome to Tic-Tac-Toe!")
        # SLEEP
        sleep(2)
        # PROMPT USERS TO SELECT "X" OR "O"
        print("Please take 10 seconds to chose who is 'X' and who is 'O'")
        # SLEEP
        sleep(10)
        # CREATE BOARD
        self.create_board()
        # RANDOMLY CHOOSE FIRST PLAYER
        player = "X" if self.get_random_first_player() == 1 else "O"
        # WHILE LOOP
        while True:
            # INFORM USERS OF CURRENT PLAYERS TURN
            print(f"Player {player} turn")
            # SHOW BOARD
            self.show_board()
            try:
                # TAKE USERS INPUT
                row, col = list(map(int, input("Enter row and column numbers of your desired move (EX: 1 1): ").split()))
                print()
                # RECORD MOVE ON BOARD
                is_spot_ok = self.fix_spot(row-1, col-1, player)
                # CHECK IF CURRENT PLAYER HAS WON
                if self.is_player_win(player):
                    print(f"Player {player} has won!")
                    break
                # CHECK FOR DRAW
                if self.is_board_filled():
                    print("Match Draw!")
                    break
                # CHECK IF ITS OKAY TO SWAP TURNS
                if is_spot_ok:
                    # SWAP TURNS
                    player = self.swap_player_turn(player)

            except ValueError:
                print("Invalid input. Please try again.")
        # SHOW FINAL VIEW OF BOARD
        print()
        self.show_board()


# START GAME
tic_tac_toe = TicTacToe()
tic_tac_toe.start()

