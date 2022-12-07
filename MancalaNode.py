import random
from MancalaBoard import State
from copy import deepcopy


MCTS_ITERATIONS = 1000


class Node:

    def __init__(self, state: State, current_player, parent=None, mouvement="", old_player=None):

        self.ranking = 0
        self.old_player = old_player
        self.player_side = current_player
        self.state = state
        self.value = None
        self.alpha = float('-inf')
        self.beta = float('inf')
        self.parent = parent
        self.best_path = None
        self.mouvement_to_child = mouvement if mouvement != "" else self.state.possible_moves(current_player)[
            random.randint(0, len(self.state.possible_moves(current_player))-1)]
        self.heuristics = {
            1: self.heuristic_1,
            2: self.heuristic_2,
            3: self.herusitic_3,
        }

    def successeurs(self):
        succ = []
        for m in self.state.possible_moves(self.player_side):
            child = deepcopy(self.state)
            current_player = child.do_move(m, self.player_side)
            node_child = Node(child, current_player,
                              self, mouvement=m, old_player=self.player_side)
            node_child.ranking = node_child.evaluate(
                monte_carlo=False, heuristic=1)
            succ.append(node_child)

        succ = sorted(succ, key=lambda x: x.ranking,
                      reverse=self.player_side == 1)
        return succ

    def random_turn(self, Game: State, current_player):
        if len(Game.possible_moves(current_player)) > 0:
            moves = Game.possible_moves(current_player)
            move = moves[random.randint(0, len(moves)-1)]
            current_player = Game.do_move(move, current_player)
            return current_player, Game

    def end_game_since(self):
        node_copy = deepcopy(self)
        game = node_copy.state
        current_player = node_copy.player_side
        while not game.game_over():
            current_player, game = self.random_turn(game, current_player)

        winner = game.find_winner()

        if winner < 0:
            return -1
        elif winner > 0:
            return 1
        else:
            return 0

    def MCTS(self):
        gain = 0
        for _ in range(MCTS_ITERATIONS):
            winner = self.end_game_since()
            if winner == self.player_side:
                gain += 1

        FMKS = gain
        return FMKS

    def herusitic_3(self):
        pass

    def heuristic_2(self):
        max_store = self.state.board_game["M1"]
        min_store = self.state.board_game["M2"]

        somme_max = 0
        somme_min = 0
        weight = 4

        for key, value in self.state.board_game.items():
            if key in self.state.possible_moves(1):
                somme_max += value
            elif key in self.state.possible_moves(-1):
                somme_min += value

        evaluation = (weight*max_store + somme_max) - \
            (weight*min_store + somme_min)
        return evaluation

    def heuristic_1(self):
        return self.state.board_game["M1"] - self.state.board_game["M2"]

    def evaluate(self, monte_carlo=False, heuristic=1):
        if not monte_carlo:
            return self.heuristics[heuristic]()
        else:
            weight = (MCTS_ITERATIONS//2)
            short_term_strategy = self.heuristics[heuristic]()
            long_term_strategy = self.MCTS()

            return weight*short_term_strategy+long_term_strategy
