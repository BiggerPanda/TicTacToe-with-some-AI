# write your code here
import random


class TicTacToe:
    board_status = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    o_amount = 0
    x_amount = 0

    def coordiates(self, x, y):
        if x == 1 and y == 1:
            return 6
        if x == 1 and y == 2:
            return 3
        if x == 1 and y == 3:
            return 0
        if x == 2 and y == 1:
            return 7
        if x == 2 and y == 2:
            return 4
        if x == 2 and y == 3:
            return 1
        if x == 3 and y == 1:
            return 8
        if x == 3 and y == 2:
            return 5
        if x == 3 and y == 3:
            return 2

    def revese_coordiates(self, x):
        if x == 6:
            return 1, 1
        if x == 3:
            return 1, 2
        if x == 0:
            return 1, 3
        if x == 7:
            return 2, 1
        if x == 4:
            return 2, 2
        if x == 1:
            return 2, 3
        if x == 8:
            return 3, 1
        if x == 5:
            return 3, 2
        if x == 2:
            return 3, 3

    def game_status(self):

        if (self.board_status[0] != ' ' and
                self.board_status[0] == self.board_status[3] and
                self.board_status[3] == self.board_status[6]):
            return self.board_status[0]
        if (self.board_status[1] != ' ' and
                self.board_status[1] == self.board_status[4] and
                self.board_status[4] == self.board_status[7]):
            return self.board_status[1]
        if (self.board_status[2] != ' ' and
                self.board_status[2] == self.board_status[5] and
                self.board_status[5] == self.board_status[8]):
            return self.board_status[2]


        if self.board_status[0] != ' ' and \
                self.board_status[0] == self.board_status[1] and \
                self.board_status[0] == self.board_status[2]:
            return self.board_status[0]
        if self.board_status[3] != ' ' and \
                self.board_status[3] == self.board_status[4] and \
                self.board_status[3] == self.board_status[5]:
            return self.board_status[3]
        if self.board_status[6] != ' ' and \
                self.board_status[6] == self.board_status[7] and \
                self.board_status[6] == self.board_status[8]:
            return self.board_status[6]


        # Main diagonal win
        if self.board_status[0] != ' ' and \
                self.board_status[0] == self.board_status[4] and \
                self.board_status[0] == self.board_status[8]:
            return self.board_status[0]

        # Second diagonal win
        if self.board_status[2] != ' ' and \
                self.board_status[2] == self.board_status[4] and \
                self.board_status[2] == self.board_status[6]:
            return self.board_status[2]

        # Is whole board full?
        for i in range(0, 9):
                # There's an empty field, we continue the game
                if self.board_status[i] == ' ':
                    return None

        # It's a tie!
        return ' '

    def board_print(self):
        print('-'*9)
        print('| ' + self.board_status[0] + " " + self.board_status[1] + " " + self.board_status[2] + ' |')
        print('| ' + self.board_status[3] + " " + self.board_status[4] + " " + self.board_status[5] + ' |')
        print('| ' + self.board_status[6] + " " + self.board_status[7] + " " + self.board_status[8] + ' |')
        print('-' * 9)

    def put_mark(self, a, b):
        status = True
        while status:
            if self.game_status() == ' ':
                return 0
            try:

                x = int(a)
                y = int(b)
                if (x < 0 or x >= 4) or (y < 0 or y > 3):
                    print("Coordinates should be from 1 to 3!")
                    return 5
                else:
                    if self.o_amount >= self.x_amount:
                        for i in range(1, 4):
                            for j in range(1, 4):
                                if i == x and j == y:
                                    if self.board_status[self.coordiates(x, y)] == ' ':
                                        self.board_status[self.coordiates(x, y)] = 'X'
                                        self.board_print()
                                        if self.game_status() == 'X' or self.game_status() == 'O':
                                            break
                                        status = False
                                        self.x_amount += 1
                                        return 0
                                    else:
                                        print('This cell is occupied! Choose another one!')
                                        return 5
                    else:
                        for i in range(1, 4):
                            for j in range(1, 4):
                                if i == x and j == y:
                                    if self.board_status[self.coordiates(x, y)] == ' ':
                                        self.board_status[self.coordiates(x, y)] = 'O'
                                        self.board_print()
                                        if self.game_status() == 'X' or self.game_status() == 'O':
                                            break
                                        status = False
                                        self.o_amount += 1
                                        return 0
                                    else:
                                        print('This cell is occupied! Choose another one!')
                                        return 5
            except ValueError:
                print("You should enter numbers!")
                return 5


class PlayGame(TicTacToe):

    player_ai = ''
    player_ai2 = ''
    player_user = ''

    def easy_bot(self):

        while True:
            if self.game_status() == ' ':
                print('Draw')
                break
            if self.game_status() == 'X' or self.game_status() == 'O':
                break

            x = random.randint(1, 3)
            y = random.randint(1, 3)
            print('Making move level "easy"')
            if self.put_mark(x, y) != 5:
                break


    def medium_bot_checks(self):
        for i in range(0, 9):
            if i == 0:
                if (self.board_status[i+1] == self.board_status[i+2] or self.board_status[i+3] ==
                        self.board_status[i+6] or
                        self.board_status[i + 4] == self.board_status[i + 8]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 1:
                if (self.board_status[i - 1] == self.board_status[i + 1] or self.board_status[i + 3] ==
                        self.board_status[i + 6]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                else:
                    return 'no move'
            if i == 2:
                if (self.board_status[i - 1] == self.board_status[i - 2] or self.board_status[i + 3] ==
                        self.board_status[i + 6] or
                        self.board_status[i + 2] == self.board_status[i + 4]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 3:
                if (self.board_status[i + 1] == self.board_status[i + 2] or self.board_status[i - 3] ==
                        self.board_status[i + 3]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 4:
                if (self.board_status[i - 1] == self.board_status[i + 1] or self.board_status[i - 3] ==
                        self.board_status[i + 3] or
                        self.board_status[i - 4] == self.board_status[i + 4]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 5:
                if (self.board_status[i - 1] == self.board_status[i - 2] or self.board_status[i - 3] ==
                        self.board_status[i + 3]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 6:
                if (self.board_status[i + 1] == self.board_status[i + 2] or self.board_status[i - 3] ==
                        self.board_status[i - 6] or
                        self.board_status[i - 2] == self.board_status[i - 4]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 7:
                if (self.board_status[i - 1] == self.board_status[i + 1] or self.board_status[i - 3] ==
                        self.board_status[i - 6]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'
            if i == 8:
                if (self.board_status[i + 1] == self.board_status[i + 2] or self.board_status[i - 3] ==
                        self.board_status[i - 6] or
                        self.board_status[i - 4] == self.board_status[i - 8]):
                    if self.board_status[i] == ' ':
                        return self.revese_coordiates(i)
                    else:
                        return 'no move'
                return 'no move'

    def medium_bot(self):
        while True:
            if self.game_status() == ' ':
                print('Draw')
                break
            if self.game_status() == 'X' or self.game_status() == 'O':
                break
            if self.medium_bot_checks() == 'no move':
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                print('Making move level "medium"')
                if self.put_mark(x, y) != 5:
                    break
            else:
                if self.game_status() == ' ':
                    print('Draw')
                    break
                print('Making move level "medium"')
                x, y = self.medium_bot_checks()
                if self.put_mark(x, y) != 5:
                    break

    def hard_bot(self, mark_of_player):
        while True:
            if mark_of_player == 'X':
                if self.game_status() == ' ':
                    print('Draw')
                    break
                if self.game_status() == mark_of_player:
                    break
                value, board_mark = self.max(mark_of_player)
                x, y = self.revese_coordiates(board_mark)
                print('Making move level "hard"')
                if self.put_mark(x, y) != 5:
                    break

            elif mark_of_player == 'O':
                if self.game_status() == ' ':
                    print('Draw')
                    break
                if self.game_status() == mark_of_player:
                    break
                value, board_mark = self.min(mark_of_player)
                x, y = self.revese_coordiates(board_mark)
                print('Making move level "hard"')
                if self.put_mark(x, y) != 5:
                    break


    def player_move(self):
        while True:
            if self.game_status() == ' ':
                print('Draw')
                break
            if self.game_status() == 'X' or self.game_status() == 'O':
                break
            x_input, y_input = input('Enter the coordinates: >').split()
            if self.put_mark(x_input, y_input) != 5:
                break

    def game_routine_pve(self, first_parameter, sec_parameter):
        game_status = True
        self.board_print()
        if first_parameter == 'easy':
            self.player_ai = 'X'
            self.player_user = 'O'
            while game_status:
                if self.game_status() == ' ':
                    break
                self.easy_bot()
                if self.game_status() == self.player_ai:
                    print(self.player_ai + ' wins')
                    break
                self.player_move()
                if self.game_status() == self.player_user:
                    print(self.player_user + ' wins')
                    break

        elif first_parameter == 'medium':
            self.player_ai = 'X'
            self.player_user = 'O'
            while game_status:
                if self.game_status() == ' ':
                    break
                self.medium_bot()
                if self.game_status() == self.player_ai:
                    print(self.player_ai + ' wins')
                    break
                self.player_move()
                if self.game_status() == self.player_user:
                    print(self.player_user + ' wins')
                    break

        elif first_parameter == 'hard':
            self.player_ai = 'X'
            self.player_user = 'O'
            while game_status:
                if self.game_status() == ' ':
                    break
                PlayGame.hard_bot(self, self.player_ai)
                if self.game_status() == self.player_ai:
                    print(self.player_ai + ' wins')
                    break
                self.player_move()
                if self.game_status() == self.player_user:
                    print(self.player_user + ' wins')
                    break

        elif first_parameter == 'user':
            if sec_parameter == 'easy':
                self.player_ai = 'O'
                self.player_user = 'X'
                while game_status:
                    if self.game_status() == ' ':
                        break
                    self.player_move()
                    if self.game_status() == self.player_user:
                        print(self.player_user + ' wins')
                        break
                    self.easy_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

            elif sec_parameter == 'medium':
                self.player_ai = 'O'
                self.player_user = 'X'
                while game_status:
                    if self.game_status() == ' ':
                        break
                    self.player_move()
                    if self.game_status() == self.player_user:
                        print(self.player_user + ' wins')
                        break
                    self.medium_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

            elif sec_parameter == 'hard':
                self.player_ai = 'O'
                self.player_user = 'X'
                while game_status:
                    if self.game_status() == ' ':
                        break
                    self.player_move()
                    if self.game_status() == self.player_user:
                        print(self.player_user + ' wins')
                        break
                    PlayGame.hard_bot(self, self.player_ai)
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

    def game_routine_pvp(self):
        game_status = True
        self.board_print()

        while game_status:
            if self.game_status() == ' ':
                break
            self.player_move()
            if self.game_status() == 'X':
                print('X wins')
                break
            self.player_move()
            if self.game_status() == 'O':
                print('O wins')
                break

    def game_routine_eve(self, first_param, sec_param):
        game_status = True
        self.board_print()

        if first_param == 'easy':
            if sec_param == 'easy':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.easy_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.easy_bot()
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break


            elif sec_param == 'medium':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.easy_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.medium_bot()
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break

            elif sec_param == 'hard':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break


                    self.easy_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.hard_bot(self.player_ai2)
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break

        elif first_param == 'medium':
            if sec_param == 'easy':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.medium_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.easy_bot()
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break


            elif sec_param == 'medium':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.medium_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.medium_bot()
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break


            elif sec_param == 'hard':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.medium_bot()
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.hard_bot(self.player_ai2)
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break

        elif first_param == 'hard':
            if sec_param == 'easy':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.hard_bot(self.player_ai)
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.easy_bot()
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break


            elif sec_param == 'medium':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.hard_bot(self.player_ai)
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.medium_bot()
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break

            elif sec_param == 'hard':
                self.player_ai = 'X'
                self.player_ai2 = 'O'
                while game_status:
                    if self.game_status() == ' ':
                        break

                    self.hard_bot(self.player_ai)
                    if self.game_status() == self.player_ai:
                        print(self.player_ai + ' wins')
                        break

                    self.hard_bot(self.player_ai2)
                    if self.game_status() == self.player_ai2:
                        print(self.player_ai2 + ' wins')
                        break


    def command_routine(self):
        routine_status = True
        while routine_status:
            self.board_status = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.o_amount = 0
            self.x_amount = 0
            command = input('Input command: >').split()
            if command[0] == 'start':
                if command[1] == 'easy' and command[2] == 'easy':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'easy' and command[2] == 'user':
                    self.game_routine_pve(command[1], command[2])
                elif command[1] == 'user' and command[2] == 'easy':
                    self.game_routine_pve(command[1], command[2])
                elif command[1] == 'user' and command[2] == 'user':
                    self.game_routine_pvp()
                elif command[1] == 'medium' and command[2] == 'medium':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'medium' and command[2] == 'user':
                    self.game_routine_pve(command[1], command[2])
                elif command[1] == 'user' and command[2] == 'medium':
                    self.game_routine_pve(command[1], command[2])
                elif command[1] == 'medium' and command[2] == 'easy':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'easy' and command[2] == 'medium':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'hard' and command[2] == 'user':
                    self.game_routine_pve(command[1], command[2])
                elif command[1] == 'user' and command[2] == 'hard':
                    self.game_routine_pve(command[1], command[2])
                elif command[1] == 'hard' and command[2] == 'easy':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'easy' and command[2] == 'hard':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'hard' and command[2] == 'medium':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'medium' and command[2] == 'hard':
                    self.game_routine_eve(command[1], command[2])
                elif command[1] == 'hard' and command[2] == 'hard':
                    self.game_routine_eve(command[1], command[2])
                else:
                    print('Bad parameters!')
            elif command[0] == 'exit':
                break
            else:
                print('Bad parameters!')

    def min(self, mark):
        if mark == "X":
            reverse_mark = 'O'
        if mark == 'O':
            reverse_mark = 'X'

        min_val = 10
        temp_val = 0
        if self.game_status() == mark: #win
            return -1, 0
        elif self.game_status() == reverse_mark: #loss
            return 1, 0
        elif self.game_status() == " ": #tie
            return 0, 0

        for i in range(0, 9):
            if self.board_status[i] == " ":
                self.board_status[i] = 'X'
                m, max_mark = self.max(mark)
                if m < min_val:
                    min_val = m
                    temp_val = i
                self.board_status[i] = " "
        return min_val, temp_val

    def max(self, mark):
        max_val = -10
        temp_val = 0
        if mark == "X":
            reverse_mark = 'O'
        if mark == 'O':
            reverse_mark = 'X'

        if self.game_status() == reverse_mark: #loss
            return -1, 0
        elif self.game_status() == mark: #win
            return 1, 0
        elif self.game_status() == " ": #tie
            return 0, 0

        for i in range(0, 9):
            if self.board_status[i] == ' ':
                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                self.board_status[i] = 'O'
                m, min_i = self.min(mark)
                # Fixing the maxv value if needed
                if m > max_val:
                    max_val = m
                    temp_val = i

                # Setting back the field to empty
                self.board_status[i] = ' '
        return max_val, temp_val


test1 = PlayGame()

test1.command_routine()

