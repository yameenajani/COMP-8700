# Solution for Q6 of Assignment 4
# Yameen Ajani - 110096721

import numpy as np
import warnings
warnings.filterwarnings("ignore")

NEGATION_CHAR = '-'
EMPTY_CHAR = ''
FAILURE = 'FAILURE'

class WalkSAT(object):
    def __init__(self, clauses):
        self.model = dict()
        self.clauses = set([])
        self.clauses = clauses
        self.get_model()

    def at(self, s, n):
        i = 0
        for e in s:
            if i == n: return e
            i += 1
    
    def get_model(self):
        symbols = set([])
        for clause in self.clauses:
            for literal in clause:
                symbols.add(self.get_symbol(literal))
        self.model = {l : bool(np.random.randint(0, 1 + 1)) for l in symbols}

    def get_symbol(self, literal):
        return literal.replace(NEGATION_CHAR, EMPTY_CHAR)

    def is_literal_satisfiable(self, literal):
        if literal.startswith(NEGATION_CHAR): return not self.model[self.get_symbol(literal)]
        return self.model[literal]
    
    def is_clause_satisfiable(self, clause):
        for literal in clause:
            if self.is_literal_satisfiable(literal): return True
        return False

    def unsatisfied_clauses(self):
        unsatisfied_clauses = 0
        for clause in self.clauses:
            if not self.is_clause_satisfiable(clause): unsatisfied_clauses += 1
        return unsatisfied_clauses

    def get_random_clause(self):
        return self.at(self.clauses, np.random.randint(0, len(self.clauses)))

    def get_random_symbol(self, clause):
        return self.get_symbol(self.at(clause, np.random.randint(0, len(clause))))

    def get_maximizing_symbol(self, clause):
        min = len(self.clauses) + 1
        for literal in clause:
            symbol = self.get_symbol(literal)
            self.model[symbol] = not self.model[symbol]
            unsatisfied_clauses = self.unsatisfied_clauses()
            if unsatisfied_clauses < min:
                min = unsatisfied_clauses
                min_symbol = symbol
            self.model[symbol] = not self.model[symbol]
        return min_symbol

    def solve(self, max_flips = 1000, p = 0.5):
        check = False
        for i in range(max_flips):
            if self.unsatisfied_clauses() == 0: return self.model
            while not check:
                clause = self.get_random_clause()
                if not self.is_clause_satisfiable(clause): check = True
            check = False
            probability = np.random.uniform()
            if probability <= p: l = self.get_random_symbol(clause)
            else: l = self.get_maximizing_symbol(clause)
            self.model[l] = not self.model[l]
        return FAILURE

def main():
    clauses1 = set([frozenset({"-D", "-B", "C"}), frozenset({"B", "-A", "-C"}), frozenset({"-C", "-B", "E"}), frozenset({"E", "-D", "B"}), frozenset({"B", "E", "-C"})])
    
    clauses2 = set([frozenset({'C', '-A', '-B'}), frozenset({'-C', 'B', 'E'}), frozenset({'-B', 'E', 'A'}), frozenset({'-E', 'C', 'A'}), frozenset({'-D', 'A', '-B'}), frozenset({'-C', '-A', '-B'}), frozenset({'C', 'D', 'B'}), frozenset({'-E', 'C', 'D'}), frozenset({'-E', 'C', '-A'}), frozenset({'D', 'B', '-A'})])

    clauses3 = set([frozenset({'-E', 'D', 'C'}), frozenset({'-D', '-A', 'C'}), frozenset({'D', '-A', 'E'}), frozenset({'D', 'E', 'C'}), frozenset({'-D', '-B', 'C'}), frozenset({'D', '-A', 'B'}), frozenset({'B', '-C', 'E'}), frozenset({'-B', 'A', 'C'}), frozenset({'D', 'A', 'C'}), frozenset({'-B', '-C', '-E'})])

    clauses4 = set([frozenset({'E', 'C', 'A'}), frozenset({'-E', 'A', '-D'}), frozenset({'C', '-E', 'D'}), frozenset({'B', '-E', 'D'}), frozenset({'E', '-C', 'B'}), frozenset({'-C', 'A', '-D'}), frozenset({'-C', '-B', '-D'}), frozenset({'E', '-C', '-D'}), frozenset({'-C', 'A', 'B'}), frozenset({'B', '-C', '-A'})])

    clauses5 = set([frozenset({'E', 'A', 'B'}), frozenset({'-B', 'E', '-D'}), frozenset({'E', '-D', '-A'}), frozenset({'E', '-D', '-C'}), frozenset({'A', 'D', 'C'}), frozenset({'B', 'E', '-C'}), frozenset({'B', 'E', '-D'}), frozenset({'A', '-E', 'C'}), frozenset({'B', '-E', '-C'}), frozenset({'-B', '-E', '-A'})])

    clauses6 = set([frozenset({'-A', 'B', 'D'}), frozenset({'A', '-B', 'D'}), frozenset({'-A', 'B', '-D'}), frozenset({'A', 'B', 'C'}), frozenset({'E', 'B', 'C'}), frozenset({'-E', '-A', 'B'}), frozenset({'A', '-E', 'C'}), frozenset({'D', '-B', 'C'}), frozenset({'E', '-C', '-B'}), frozenset({'E', '-C', 'B'})])

    clauses7 = set([frozenset({'-B', 'D', 'E'}), frozenset({'D', 'B', '-E'}), frozenset({'C', 'E', 'B'}), frozenset({'-B', '-A', '-E'}), frozenset({'D', '-A', '-E'}), frozenset({'-C', '-D', '-B'}), frozenset({'C', '-A', '-D'}), frozenset({'-E', 'B', 'C'}), frozenset({'-A', 'E', '-D'}), frozenset({'-A', 'D', 'C'})])

    clauses8 = set([frozenset({'E', '-A', '-C'}), frozenset({'B', 'E', '-A'}), frozenset({'A', '-E', '-C'}), frozenset({'A', 'D', 'C'}), frozenset({'-B', 'D', 'C'}), frozenset({'-E', '-D', 'C'}), frozenset({'-E', '-B', '-C'}), frozenset({'A', '-B', 'E'}), frozenset({'-D', '-B', '-A'}), frozenset({'-C', '-B', '-A'})])

    clauses9 = set([frozenset({'E', '-A', '-B'}), frozenset({'-D', '-B', '-E'}), frozenset({'E', '-D', 'C'}), frozenset({'A', '-D', '-E'}), frozenset({'D', '-B', '-E'}), frozenset({'-A', 'D', '-C'}), frozenset({'A', 'D', '-E'}), frozenset({'A', 'E', '-C'}), frozenset({'A', '-C', '-E'}), frozenset({'B', 'D', '-E'})])

    clauses10 = set([frozenset({'-B', '-C', 'A'}), frozenset({'-D', 'A', 'B'}), frozenset({'D', '-C', 'A'}), frozenset({'-C', 'A', 'B'}), frozenset({'-C', 'A', 'E'}), frozenset({'-B', 'A', '-E'}), frozenset({'B', 'C', 'E'}), frozenset({'D', 'A', '-E'}), frozenset({'D', '-B', '-E'}), frozenset({'-D', '-A', 'B'})])

    for i in range(1, 11):
        print("Solving for clause set {}".format(i))
        solver = WalkSAT(eval("clauses{}".format(i)))
        result = solver.solve()
        if result == FAILURE: print("Couldn't figure out satisfiability.")
        else: print(str(result))


if __name__ == '__main__':
    main()