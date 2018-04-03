/* S3C2 Russell */
writeList([]).
writeList([H|T]) :-
	write(H),nl,writeList(T).