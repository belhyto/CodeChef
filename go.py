import numpy as np
import copy
import random
import time

class GoGame:
    def __init__(self, board_size=9):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)
        self.current_player = 1  # 1 for black, 2 for white
        self.pass_count = 0
        self.move_history = []

    def get_legal_moves(self):
        return [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.is_valid_move(i, j)]

    def is_valid_move(self, i, j):
        if self.board[i, j] != 0:
            return False
        test_board = copy.deepcopy(self.board)
        test_board[i, j] = self.current_player
        return self.has_liberty(test_board, i, j)

    def has_liberty(self, test_board, i, j):
        board_size = len(test_board)
        player = test_board[i, j]
        visited = np.zeros((board_size, board_size), dtype=bool)

        def dfs(x, y):
            if x < 0 or x >= board_size or y < 0 or y >= board_size:
                return False
            if visited[x, y]:
                return True
            if test_board[x, y] == 0:
                return True
            if test_board[x, y] != player:
                return False
            visited[x, y] = True
            return dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1)

        return dfs(i, j)

    def make_move(self, i, j):
        if not self.is_valid_move(i, j):
            raise ValueError("Invalid move")
        self.board[i, j] = self.current_player
        self.move_history.append((i, j))
        self.current_player = 3 - self.current_player  # Switch player
        self.pass_count = 0

    def pass_turn(self):
        self.pass_count += 1
        self.current_player = 3 - self.current_player  # Switch player

    def is_game_over(self):
        return self.pass_count >= 2

    def count_score(self):
        black_territory = 0
        white_territory = 0
        black_stones = 0
        white_stones = 0

        board_size = len(self.board)
        visited = np.zeros((board_size, board_size), dtype=bool)

        def dfs(x, y):
            if x < 0 or x >= board_size or y < 0 or y >= board_size:
                return
            if visited[x, y]:
                return
            visited[x, y] = True
            if self.board[x, y] == 0:
                if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
                    return True
                return False
            elif self.board[x, y] == 1:
                return True
            elif self.board[x, y] == 2:
                return False

        for i in range(board_size):
            for j in range(board_size):
                if self.board[i, j] == 0 and not visited[i, j]:
                    if dfs(i, j):
                        black_territory += 1
                    else:
                        white_territory += 1
                elif self.board[i, j] == 1:
                    black_stones += 1
                elif self.board[i, j] == 2:
                    white_stones += 1

        black_score = black_territory + black_stones
        white_score = white_territory + white_stones
        return black_score, white_score

    def get_winner(self):
        black_score, white_score = self.count_score()
        if black_score > white_score:
            return "Black wins"
        elif white_score > black_score:
            return "White wins"
        else:
            return "Tie"

    def display_board(self):
        symbols = ['.', 'X', 'O']
        for i in range(self.board_size):
            row = ' '.join(symbols[x] for x in self.board[i])
            print(row)
        print()

class MonteCarloTreeSearch:
    def __init__(self, exploration_constant=1.4):
        self.exploration_constant = exploration_constant

    def select_move(self, game, simulations=1000):
        root = Node(game)
        for _ in range(simulations):
            node = root
            simulation_game = copy.deepcopy(game)

        # Select
            while node.children:
                node = self.select_best_child(node)
                simulation_game.make_move(*node.move)

        # Expand
            if not simulation_game.is_game_over():
                legal_moves = simulation_game.get_legal_moves()
                if not legal_moves:
                    break  # No legal moves available
                chosen_move = random.choice(legal_moves)
                simulation_game.make_move(*chosen_move)
                node = node.add_child(chosen_move, simulation_game)

        # Simulate
            while not simulation_game.is_game_over():
                legal_moves = simulation_game.get_legal_moves()
                if not legal_moves:
                    break  # No legal moves available
                chosen_move = random.choice(legal_moves)
                simulation_game.make_move(*chosen_move)

        # Backpropagate
            result = simulation_game.count_score()[game.current_player - 1]
            while node:
                node.visits += 1
                node.wins += result
                node = node.parent

        best_child = self.select_best_child(root)
        return best_child.move if best_child else None


    def select_best_child(self, node):
      best_score = float("-inf")
      best_children = []
      for child in node.children:
            score = child.wins / child.visits + self.exploration_constant * np.sqrt(np.log(node.visits) / child.visits)
            if score > best_score:
                best_score = score
                best_children = [child]
            elif score == best_score:
                best_children.append(child)
      if not best_children:
            return None  # No children available
      return random.choice(best_children)


class Node:
    def __init__(self, game, parent=None, move=None):
        self.game = game
        self.parent = parent
        self.move = move
        self.visits = 0
        self.wins = 0
        self.children = []

    def add_child(self, move, game):
        child = Node(game, self, move)
        self.children.append(child)
        return child

def play_game():
    game = GoGame()
    mcts = MonteCarloTreeSearch()

    while not game.is_game_over():
        game.display_board()

        if game.current_player == 1:
            i, j = map(int, input("Enter your move (row col): ").split())
            game.make_move(i, j)
        else:
            print("AI is thinking...")
            start_time = time.time()
            i, j = mcts.select_move(game)
            print("AI move:", i, j)
            game.make_move(i, j)
            print("AI move time:", time.time() - start_time)

    game.display_board()
    print("Game over")
    print(game.get_winner())

if __name__ == "__main__":
    play_game()
