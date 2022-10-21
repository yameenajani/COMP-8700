from utils import *

depth = 20
success = False
states = list()
visited_states = set()


def dfs():
    initial_state = (3, 3, 1)
    visited_states.add(initial_state)
    states = [initial_state]
    root_node = "0" + str(initial_state) + "0"

    new_states = get_boat_left_next_states(initial_state)
    goto_next_depth(new_states, 1, states, root_node)


def handle_success(prob_state, state_stack):
    global success
    state_stack.append(prob_state)
    print("Solution found!")
    print("The following sequence of states leads to a solution:")
    for state in state_stack:
        print(state)
    success = True


def get_next_states(prob_state):
    new_states = []
    if boat_left(prob_state):
        new_states = get_boat_left_next_states(prob_state)
    elif boat_right(prob_state):
        new_states = get_boat_right_next_states(prob_state)
    return new_states


def handle_fail(prob_state, state_stack, current_depth, parent_node_id):
    state_stack.append(prob_state)
    new_states = get_next_states(prob_state)
    not_duplicate_states = []
    for new_state in new_states:
        if new_state not in visited_states:
            visited_states.add(new_state)
            not_duplicate_states.append(new_state)
    goto_next_depth(not_duplicate_states, current_depth + 1, state_stack, parent_node_id)
    state_stack.pop()


def goto_next_depth(same_level_states, current_depth, state_stack, parent_node_id):
    global success
    for index, prob_state in enumerate(same_level_states):
        if not success:
            visited_states.add(prob_state)
            current_node_id = get_current_node_id(prob_state, current_depth, index, parent_node_id)
            if is_success(prob_state):
                handle_success(prob_state, state_stack)
            elif current_depth < depth:
                handle_fail(prob_state, state_stack, current_depth, current_node_id)


def get_current_node_id(prob_state, current_depth, index, parent_node_id):
    current_node_id = parent_node_id + str(current_depth) + str(prob_state) + str(index)
    return current_node_id


if __name__ == "__main__":
    dfs()
