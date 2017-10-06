import functools
import time
import itertools

def product(x):
	return functools.reduce(lambda a,b: a*b, x)

def factorial(n):
	return product(range(1,n+1))

def ncr(n,r):
	if r==0 or r==n:
		return 1
	if n-r > r:
		return ncr(n,n-r)
	if r > n:
		return 0
	result = product(range(r+1,n+1))
	for i in range(1,(n-r)+1):
		result = result // i
	return result

def intpartlim(N, M, n):
	if n < 0:
		return 0
	if n==0:
		return 1
	if M==1:
		return 1 if n <= N else 0
	if N==1:
		return 1 if n <= M else 0
	return intpartlim(N,M-1,n) + intpartlim(N-1,M,n-M)

# number of ways to write n as a sum of natural numbers
def intpart(n):
	return intpartlim(n,n,n)

# number of partions of {1,2,...,n}
def bell(n):
	if n < 2:
		return 1
	result = 0
	for k in range(n):
		result += ncr(n-1,k)*bell(k)
	return result

#primesBelow5000 = [2, 3, 5, 7, 11, 13, 17, 19]
#print(list(filter(isprime, range(2,5000))))

primesBelow5000 = [] # LOL

precomputedP = primesBelow5000

precomputedPmax = (precomputedP[-1] // 6)*6-1
while precomputedP[-1] >= precomputedPmax:
	precomputedP.pop(-1)

#print(precomputedP)
#print(precomputedPmax)

def isprime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n & 1 == 0:
		return False
	
	if n < precomputedPmax:
		return n in precomputedP
	for prime in precomputedP:
		if n % prime == 0:
			return False
	i = precomputedPmax
	while i < n and n % i != 0:
		i += 2
		if i < n and n % i == 0:
			return False
		i += 2
	return i >= n

def getprimefactors(n):
	if n in precomputedP:
		yield n
		return
	while n&1==0:
		yield 2
		n = n >> 1
	i = 3
	while n != 1:
		if n % i == 0:
			n = n // i
			yield i
		else:
			i += 2

def getfactors(n):
	if n in precomputedP:
		yield 1
		yield n
		return
	yield from filter(lambda i: n%i==0, range(1,n+1))
	return

def precompute(func, dic, x):
	if x in dic:
		return dic[x]
	result = func(x)
	dic[x] = result
	return result

def permutations(x):
	return itertools.permutations(x)
'''
def permutations(x):
	yield x
	i = 0
	n = len(x)
	c = [0]*n
	while i < n:
		if c[i] < i:
			if i & 1 == 0:
				x[0],x[i] = x[i],x[0]
			else:
				x[c[i]],x[i]=x[i],x[c[i]]
			yield x
			c[i] += 1
			i = 0
		else:
			c[i] = 0
			i += 1
'''
def combinations(x):
	for k in range(len(x)+1):
		yield from kcombinations(x,k)

def kcombinations(x,k):
	return itertools.combinations(x,k)
'''
def combinations(x):
	n = len(x)
	for i in range(2**n):
		output = []
		index = 0
		while i != 0:
			if i&1==1:
				output.append(x[index])
			i = i >> 1
			index += 1
		yield output

# USE itertools.combinations INSTEAD
def kcombinations(x,k):
	if k == 0:
		yield []
		return
	if k == 1:
		for item in x:
			yield [item]
		return
	n = len(x)
	if n == k:
		yield x
		return
	for remainder in kcombinations(x[1:],k-1):
		yield [x[0]] + remainder
	yield from kcombinations(x[1:],k)
'''

def getintpartlim(N, M, n):
	if n < 0:
		return
	if n==0:
		yield []
		return
	if M==1:
		if n <= N:
			yield [n]
		return
	if N==1:
		if n <= M:
			yield [1]*n
		return
	yield from getintpartlim(N-1,M,n)
	for remainder in getintpartlim(N,M-1,n-N):
		yield [N] + remainder

def getintpart(n):
	return getintpartlim(n,n,n)

def getsettings(n, k):
	i = 0
	while True:
		temp = i
		result = [0]*n
		for index in range(n):
			result[index] = temp % k
			temp = temp // k
		if temp != 0:
			return
		yield result
		i += 1


print([list(i) for i in combinations([1,2,3])])
print([list(i) for i in kcombinations([1,2,3,4,5],3)])
print([i for i in permutations([1,2,3])])
print([list(i) for i in getintpart(5)])
print([list(i) for i in getsettings(2,3)])
print(list(getfactors(24)))


summ = 0
'''
for i in range(100):
	for c in kcombinations(list(range(20)), 5):
		summ += c[0]

for i in range(100):
	for c in itertools.combinations(list(range(20)), 5):
		summ += c[0]


for i in range(1):
	x = list(range(10))
	for c in permutations(x):
		summ += x[0]
'''
for i in range(1):
	for c in itertools.permutations(list(range(10))):
		summ += c[0]
'''

for i in range(100):
	for c in combinations(list(range(12))):
		summ += sum(c)

for i in range(100):
	for k in range(20+1):
		for c in itertools.combinations(list(range(12)), k):
			summ += sum(c)
'''
print(summ)


#print(False in [isprime(i) == (i in primesBelow3500) for i in range(3500)])



'''
TODO:
Way to loop through
-combinations
-intpart

Way to precompute any function
-recursively
'''
