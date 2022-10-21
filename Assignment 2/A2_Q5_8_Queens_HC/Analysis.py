import numpy as np
from HillClimbing import HillClimbing
import warnings
import sys

NUM_STATES = 1000
ALGOS = ['Steepest-Ascent Hill Climbing', 'Steepest-Ascent Hill Climbing (with 100 sidesteps)']

def generate_state():
    return np.random.randint(8, size=8)

def print_results(num_moves, fail_moves):
    print("\nResults:")
    for algo_name in ALGOS:
        print(algo_name)
        print('-'*15)
        result_string = "Solved {} of {} instances (Success rate - {:.2f}%).\nAverage # of moves when it succeeds : {:.0f}\nAverage # of moves when it fails : {:.0f}\n"\
                        .format(len(num_moves[algo_name]), NUM_STATES, len(num_moves[algo_name])/NUM_STATES*100, np.mean(num_moves[algo_name]), np.mean(fail_moves[algo_name]))
        print(result_string)

def update_progress(progress, total):
    percent  = progress/total*100
    sys.stdout.write('\r[{}] {:.2f}% {}/{} cases'.format('*'*int(percent/5)+'-'*(20-int(percent/5)), percent, progress, total))

if __name__ == "__main__":
    np.random.seed(42)

    num_moves = {algo: [] for algo in ALGOS}
    fail_moves = {algo: [] for algo in ALGOS}

    # Generate random state
    states = [generate_state() for i in range(NUM_STATES)]

    print("Running algorithms...")
    for i, state in enumerate(states):
        # Solve with Hill Climbing
        hill = HillClimbing(state)
        # Steepest Ascent
        end_state, end_cost, is_plateau, moves = hill.steepest_ascent()
        if(end_cost == 0): num_moves[ALGOS[0]].append(moves)
        else: fail_moves[ALGOS[0]].append(moves)
        # Steepest Ascent with 100 sidesteps
        end_state, end_cost, is_plateau, moves = hill.first_choice(100)
        if(end_cost == 0): num_moves[ALGOS[1]].append(moves)
        else: fail_moves[ALGOS[1]].append(moves)

        update_progress(i+1, NUM_STATES)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        print_results(num_moves, fail_moves)