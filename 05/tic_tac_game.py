class TicTacGame:

    def __init__(self):
        self.board = [0] * 9

    def show_board(self, show_numeration=False):
        n = 3
        print("╭", ("───┬" * n)[:-1], "╮", sep="")
        for i in range(n):
            if i != 0:
                print("├", ("───┼" * n)[:-1], "┤", sep="")
            out = "│ "
            for j in range(n):
                if self.board[3 * i + j] == 1:
                    token = "x"
                if self.board[3 * i + j] == -1:
                    token = "o"
                if self.board[3 * i + j] == 0:
                    token = " "
                out += (str(3 * i + j) if show_numeration else token) + " │ "
            print(out, sep="")
        print("╰", ("───┴" * n)[:-1], "╯", sep="")

    def validate_move(self, move):
        if not move.isdigit() or move.startswith("-"):
            print("Input should be positive integer number.")
            return False
        idx = int(move)
        if idx not in range(9):
            print("Input should be from 0 to 8.")
            return False
        if self.board[idx] != 0:
            print(f"Board cell '{idx}' should be empty.")
            return False
        return True

    def do_move(self, move, is_crosses_move):
        idx = int(move)
        self.board[idx] = 1 if is_crosses_move else -1

    def start_game(self, show_board=True):
        endgame = None
        is_crosses_move = True
        while endgame is None:
            is_valid_move = False
            while not is_valid_move:
                move = input("Crosses' move: " if is_crosses_move else "Zeros' move: ")
                is_valid_move = self.validate_move(move)
            self.do_move(move, is_crosses_move)
            is_crosses_move = not is_crosses_move
            endgame = self.check_endgame()
            if show_board:
                self.show_board()
        print()
        if endgame == 1:
            print("Crosses win!")
        elif endgame == -1:
            print("Zeros win!")
        else:
            print("Draw!")

    def check_endgame(self):
        if self.check_winner(is_crosses=True):
            return 1
        if self.check_winner(is_crosses=False):
            return -1
        if all(x != 0 for x in self.board):
            return 0
        return None

    def check_winner(self, is_crosses):
        val = 1 if is_crosses else -1
        return True if all(x == val for x in self.board[0:3]) or \
                       all(x == val for x in self.board[3:6]) or \
                       all(x == val for x in self.board[6:9]) or \
                       all(x == val for x in self.board[0:7:3]) or \
                       all(x == val for x in self.board[1:8:3]) or \
                       all(x == val for x in self.board[2:9:3]) or \
                       all(x == val for x in self.board[0:9:4]) or \
                       all(x == val for x in self.board[2:7:2]) else False


def main():
    game = TicTacGame()
    game.show_board(show_numeration=True)
    game.start_game()


if __name__ == "__main__":
    main()
