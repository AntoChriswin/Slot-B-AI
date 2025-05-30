move(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source), write(' to '), write(Target), nl.

move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(M, Auxiliary, Target, Source).
tower_of_hanoi(N) :-
    move(N, 'peg A', 'peg C', 'peg B').
