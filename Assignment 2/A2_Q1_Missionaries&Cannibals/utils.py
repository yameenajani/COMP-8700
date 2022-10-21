import numpy as np
import math

def is_success(prob_state):
    return prob_state[0] == prob_state[1] == 0


def boat_left(prob_state):
    return prob_state[2] == 1


def boat_right(prob_state):
    return prob_state[2] == 0


def get_boat_left_next_states(prob_state):
    new_states = []
    for missionary in range(prob_state[0] + 1):
        for cannibal in range(prob_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (prob_state[0] - missionary,
                         prob_state[1] - cannibal,
                         0)
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states


def get_boat_right_next_states(prob_state):
    new_states = []
    for missionary in range(3 - prob_state[0] + 1):
        for cannibal in range(3 - prob_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (prob_state[0] + missionary,
                         prob_state[1] + cannibal,
                         1)
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states


def find_best_frontier(frontier_states, side, compute_fn):
    min_value = 100000
    min_state = -1
    for state in frontier_states:
        if state[2] != side:
            continue
        fn = compute_fn(state)
        if fn < min_value:
            min_value = fn
            min_state = state
    return min_state, min_value