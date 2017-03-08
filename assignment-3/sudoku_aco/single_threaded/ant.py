import threading
import copy
import random
import numpy as np

from sudoku_utils import *


class Ant(object):
    def __init__(self, id, alpha, beta, sudoku_matrix, pheromone_matrix):
        super().__init__()
        self.id = id
        self.alpha = alpha
        self.beta = beta
        self.sudoku_matrix = copy.deepcopy(sudoku_matrix)
        self.original_sudoku_matrix = copy.deepcopy(sudoku_matrix)
        self.pheromone_matrix = pheromone_matrix
        self.solution = []  # is used for appying pheromone update
        self.score = 0

    # same as run-method in multithreaded ant
    def find_solution(self):

        empty_positions = get_empty_positions(self.sudoku_matrix)

        for position in empty_positions:

            candidate_digits = get_possible_digits_at_position(position[0], position[1], self.sudoku_matrix)

            if candidate_digits is not None and len(candidate_digits) != 0:
                # choose digit based on pheromone value

                # solution triple = (x,y,digit)
                solution_triple = self._get_next(position[0], position[1], candidate_digits)
                self.solution.append(solution_triple)

                set_digit_at_position(position[0], position[1], solution_triple[2], self.sudoku_matrix)

        #print("Ant with id {} scored: {}\n{}".format(self.id, calculate_score(self.sudoku_matrix), self.sudoku_matrix))
        #print("Ant with id {} scored {}".format(self.id, self.get_score()))
        return self.solution

    def reset(self):
        self.sudoku_matrix = copy.deepcopy(self.original_sudoku_matrix)
        self.score = 0
        self.solution = []

    def get_score(self):
        self.score = calculate_score(self.sudoku_matrix)
        return self.score

    def _get_next(self, x, y, possible_digits):

        roulette_wheel = 0
        heuristic_total = 1

        for possible_digit in possible_digits:
            roulette_wheel += pow(self.pheromone_matrix[possible_digit - 1][x][y], self.alpha) * \
                              pow((heuristic_total / (1 / len(possible_digits))), self.beta)

        random_value = random.uniform(0, roulette_wheel)
        wheel_position = 0

        for possible_digit in possible_digits:
            wheel_position += pow(self.pheromone_matrix[possible_digit - 1][x][y], self.alpha) * \
                              pow((heuristic_total / (1 / len(possible_digits))), self.beta)
            if wheel_position >= random_value:
                return (x, y, possible_digit)




