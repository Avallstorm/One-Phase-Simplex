import math
from operator import add

#Biggest long
BIG = 9223372036854775807

#Divides every element in a list by div
#Input: List of Float, Float
#Return: List of Float

def lidivide(li,div):
	li = [num/div for num in li]
	return li

#Multiplies every element in a list by mul
#Input: List of Float, Float
#Return: List of Float

def limulti(li,mul):
	li = [num*mul for num in li]
	return li

#Adds two lists together element wise
#Input: List of Float, List of Float
#Return: List of Float
def liadd(li1, li2):
	return list(map(add,li1,li2))

#As described below
def isolateHelp(vect,equ,var):
		equ = lidivide(equ,vect[var])
		vect = lidivide(vect,vect[var])
		for i in range(len(vect)):
			if i != var:
				equ[i] = equ[i]-vect[i]
				vect[i] = 0
		return (vect,equ)

#Takes an equation of the form 
#	a + a1x1 + a2x2 + ... + anxn = b + b1x1 + b2x2 + ... + bnxn 
#	and isolates the var-th variable
#Wrapper function for isolateHelp
#Input: List of Float, List of Float, Int
#Return: List of Float, List of Float

def isolate(vect,equ,var):
	if vect[var] == 0 and equ[var] == 0:
		return None
	else:
		vect[var] = vect[var] - equ[var]
		equ[var] = 0
		return isolateHelp(vect, equ, var)

#Rounds num to the dec'th decimal place by string truncation
#Input: Float, Int
#Return: Float
def round(num,dec):
    working = str(num)
    point = None
    for i in range(len(working)):
    	if working[i] == '.':
    		point = i
    if point == None:
    	return str(num)
    if num == 0:
    	return '0'
    working = working[point:dec+2]
    return str(int(num)) + working

#Takes a list and prints it as a pretty equations where each item in the list
#	is the coefficient of a variable execpt the first which is a value
#   [a,a1,a2,...,an] ->print-> a + a1(x1) + a2(x2) + ... + an(xn)
def eqprthelp(vect):
	printstr = ''
	for i in range(len(vect)):
		if i == 0 and vect[i] != 0:
			printstr = printstr + '%s ' % round(vect[i],3)
		elif vect[i] > 0:
			if vect[i] == 1:
				if printstr == '':
					printstr = printstr + 'x%d ' % (i)
				else:
					printstr = printstr + '+ x%d ' % (i)
			else:
				if printstr == '':
					printstr = printstr + '%s*x%d ' % (round(vect[i],3),i)
				else:
					printstr = printstr + '+ %s*x%d ' % (round(vect[i],3),i)
		elif vect[i] < 0:
			if vect[i] == -1:
				if printstr == '':
					printstr = printstr + '- x%d ' % (i)
				else:
					printstr = printstr + '- x%d ' % (i)
			else:
				if printstr == '':
					printstr = printstr + '- %s*x%d ' % (round(-vect[i],3),i)
				else:
					printstr = printstr + '- %s*x%d ' % (round(-vect[i],3),i)
	return printstr

#Wrapper function for eqprthelp, described above

def equationPrint(vect,equ):
	return eqprthelp(vect) + '= ' + eqprthelp(equ)


def printdic(equ,res,ite):
	print('Dictionairy number %d' % ite)
	print(equationPrint(equ[0],equ[1]))
	print('')
	for rest in res:
		print(equationPrint(rest[0],rest[1]))
	print('')

def enteringBasis(li):
	for i in range(len(li)-1):
		if li[i+1] > 0:
			print('x%d will be entering the basis' % (i+1))
			return i+1


def leavingBasis(res1,entBas):
	#variable to store the location of the biggest value for entBas
	mini = [None,BIG]
	#list to store the inequalities when all variables but entBas are 0
	inres = []

	#Copying res1 to another set of inequality equations as mentioned above
	for rest1 in res1:
		inrest1 = []
		inrest = [rest1[0],inrest1]
		for i in range(len(rest1[1])):
			if i != entBas and i != 0:
				inrest1.append(0)
			else:
				inrest1.append(rest1[1][i])
		inres.append(inrest)

	for i in range (len(inres)):
		ineq = inres[i]
		inque = equationPrint(ineq[0],ineq[1]) + ' <= 0'
		if ineq[1][entBas] > 0:
			xlim = -(ineq[1][0]/ineq[1][entBas])
			inque = inque + ' implies that x%d >= %s' % (entBas,round(xlim,4))
		else:
			xlim = -(ineq[1][0]/ineq[1][entBas])
			if xlim < mini[1]:
				mini[0] = i
				mini[1] = xlim
			inque = inque + ' implies that x%d <= %s' % (entBas,round(xlim,4))
		print(inque)
	if mini[1] == BIG:
		return None
	else:
		leaBas = inres[mini[0]][0]
		for i in range(len(leaBas)):
			if leaBas[i] != 0:
				print('x%d will be leaving the basis\n' % i)
				return mini[0]

#simplex takes a list of and equationa and a list of equation restraints
#	and preforms the simplex algorithm on them
def simplex(equ,res):

	#Keeping track of iterations
	iteration = 1

	#isolating the last variable in the objective function
	equ = list(isolate(equ[0],equ[1],len(equ[0])-1))
	while 1:

		#Printint dictionairy for current iteration
		printdic(equ,res,iteration)

		#Checking for optimality
		if all(i <= 0 for i in equ[1][1:]):
			print('SIMPLEX COMPLETE, LP OPTIMAL')
			break

		#Printing and determinging which variables enter and leave the basis
		entBas = enteringBasis(equ[1])
		leaBas = leavingBasis(res,entBas)

		#Checking for unboundedness 
		if leaBas == None:
			print('SIMPLEX COMPLETE, LP UNBOUNDED')
			break

		(res[leaBas][0],res[leaBas][1]) = isolate(res[leaBas][0],\
			res[leaBas][1],entBas)

		for i in range(len(res)):
			if i != leaBas:
				rest = res[i]
				coef = rest[1][entBas]
				rest[1][entBas] = 0
				rest[1] = liadd(limulti(res[leaBas][1],coef),rest[1])

		coef = equ[1][entBas]
		equ[1][entBas] = 0
		adder = limulti(res[leaBas][1],coef)
		equ[1] = liadd(adder,equ[1])
		iteration = iteration + 1

'''
Note that OF is the objective funtion and it is in len(OF[0]) - 2 variables
the first element in the list is the contant and the last element in the list
Is the total of the objective function and is only to be used for OF.


For example the below code models the linear program that follows:
 maximize
 f(x1,x2,x3,x4) = 3*x1 + 4*x4 (This is shown with x5 instead of f())
 subject to
 x3 = 40 - x1 - x2
 x4 = 60 + x1 - x2


OF = [	 [0,0,0,0,0,1],[0,3,4,0,0,0]]
ST = [	[[0,0,0,1,0,0],[40,-1,-1,0,0,0]],
		[[0,0,0,0,1,0],[60,1,-1,0,0,0]]]
'''

OF = None
ST = None

def main():
	simplex(OF,ST)

if __name__ == '__main__':
	main()


