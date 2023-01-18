from copy import deepcopy
from MancalaNode import Node


class Chromosome:
    def __init__(self, genes) -> None:
        self.genes = genes if genes else None
        self.evaluation = None
        self.stores = {
            1: "M1",
            -1: "M2",
        }

    def set_evaluation(self, player_side):
        self.evaluation = self.genes[player_side]-self.genes[-player_side]


class Evolution:
    def __init__(self, noeud: Node) -> None:
        self.noeud = noeud

    def generate_population(self):
        population = []
        current_player = self.noeud.player_side
        possible_moves = self.noeud.state.possible_moves(current_player)

        clone_state = deepcopy(self.noeud)

        for move in possible_moves:
            next_player = clone_state.state.do_move(move)
            child = Node(clone_state, next_player, self.noeud,
                         mouvement=move, old_player=self.noeud.player_side)
            population.append(child.state.board_game)

        return population
