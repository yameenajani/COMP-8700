from utils import *

depth = 20
success = False
side = 1


def best_first():
    initial_state = (3, 3, 1)
    frontier_states = list()
    frontier_states.append(initial_state)
    iterate_over_states(frontier_states, 0)


def iterate_over_states(frontier_states, current_depth):
    global success
    while not success:
        best_frontier_state, best_frontier_fn = find_best_frontier(frontier_states, side, compute_fn)
        toggle_side()

        print("Frontiers: " + str(frontier_states))
        print("Best State: " + str(best_frontier_state))
        print("Best Value: " + str(best_frontier_fn))
        print("")
        frontier_states.remove(best_frontier_state)

        if is_success(best_frontier_state):
            print("Success! Goal state: " + str(best_frontier_state))
            success = True
        elif boat_left(best_frontier_state):
            add_new_states_to_frontier(frontier_states, get_boat_left_next_states(best_frontier_state))
        elif boat_right(best_frontier_state):
            add_new_states_to_frontier(frontier_states, get_boat_right_next_states(best_frontier_state))

        iterate_over_states(frontier_states, current_depth + 1)


def add_new_states_to_frontier(frontier_states, new_states):
    frontier_states += new_states


def toggle_side():
    global side
    if side == 1:
        side = 0
    else:
        side = 1


def compute_fn(prob_state):
    return compute_hn(prob_state)


def compute_hn(prob_state):
    return prob_state[0] + prob_state[1]


if __name__ == "__main__":
    best_first()
