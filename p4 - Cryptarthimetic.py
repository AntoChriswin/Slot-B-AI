from itertools import permutations

def is_valid(assignment):
    S, E, N, D, M, O, R, Y = assignment
    return (S != 0 and M != 0) and (1000*S + 100*E + 10*N + D) + (1000*M + 100*O + 10*R + E) == (10000*M + 1000*O + 100*N + 10*E + Y)

def solve_crypt_arithmetic():
    digits = range(10)
    for perm in permutations(digits, 8):
        if is_valid(perm):
            S, E, N, D, M, O, R, Y = perm
            print(f"SEND + MORE = MONEY: {S}{E}{N}{D} + {M}{O}{R}{E} = {M}{O}{N}{E}{Y}")

solve_crypt_arithmetic()
