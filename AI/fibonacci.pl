/*fibonacci of 1 is 1*/
fib(0, 0).

/*fibonacci of 1 is 1*/
fib(1, 1).

/*else*/
fib(N,F) :-
	/*if n is greater than 1*/
	N > 1,
	
	/*n1 = n-1*/
	N1 is N-1,

	/*n2 = n-2*/
	N2 is N-2,

	/*call recursively for n1*/
	fib(N1, F1),

	/*call recursively for n1*/
	fib(N2, F2),

	/*add fibonacci number*/
	F is F1 + F2.
/* to run the code consult select this file and fib(any number,Y)*/


