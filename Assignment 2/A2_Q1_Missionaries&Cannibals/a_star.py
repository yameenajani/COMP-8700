from utils import *

states_gn = dict()
success = False
side = 1


def a_star():
    initial_state = (3, 3, 1)
    frontier_states = set()
    frontier_states.add(initial_state)
    states_gn[initial_state] = 0
    iterate_over_states(frontier_states, 1, 0)


def iterate_over_states(frontier_states, current_gn_cost, current_depth):
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
            a_states = get_boat_left_next_states(best_frontier_state)
            add_new_states_to_frontier(frontier_states, a_states, current_gn_cost)
        elif boat_right(best_frontier_state):
            b_states = get_boat_right_next_states(best_frontier_state)
            add_new_states_to_frontier(frontier_states, b_states, current_gn_cost)
        iterate_over_states(frontier_states, current_gn_cost + 1, current_depth + 1)


def add_new_states_to_frontier(frontier_states, new_states, current_gn_cost):
    for state in new_states:
        states_gn[state] = current_gn_cost
        frontier_states.add(state)


def toggle_side():
    global side
    if side == 1:
        side = 0
    else:
        side = 1


def compute_fn(prob_state):
    return compute_gn(prob_state) + compute_hn(prob_state)


def compute_hn(prob_state):
    return prob_state[0] + prob_state[1]


def compute_gn(prob_state):
    return states_gn[prob_state]


if __name__ == "__main__":
    a_star()
