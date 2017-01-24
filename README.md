# One-Phase-Simplex
Implementation of the one phase simplex algorithm with every step printed. Useful for CO 250 at University of Waterloo.

The main file is simplex.py, currently to use it you will need to open it in an editor and change the OF and ST variables according the to the following example.

OF = [   [0,0,0,0,0,1],[0,3,4,0,0,0]]
ST = [  [[0,0,0,1,0,0],[40,-1,-1,0,0,0]],
        [[0,0,0,0,1,0],[60,1,-1,0,0,0]]]

This will model the followin linear problem:

f(x1,x2,x3,x4) = 3*x1 + 4*x4
subject to
x3 = 40 - x1 - x2
x4 = 60 + x1 - x2

The algorithm supports any number of variables and restricing functions but will only detect for Unboundedness and Optimality.

This is still in fairly early stages of development, I first created it to check my work in a class so it was only just barely usable.

Created by Ava Stos