def fib(size):
	alist = [0,1]
	if (size < 2):
		return alist[:size]


	for i in range(2,size):
		alist.append(alist[i-1] + alist[i-2])
	return alist


def sumevenfib_old(size):
	# Returns the sum of all even numbers in a fibonacci sequence of 'size'.

	flist = fib(size)[0::3] # Get a list of fibonacci numbers and then return only the even numbers of that list.
	total = 0
	for item in flist:
		total += item
	return total


def sumevenfib(size):
	# Returns the sum of all even numbers in a fibonacci sequence of 'size'.
	total = 0
	a=0
	b=1
	c=1
	for i in range(0,size,3):
		total += a
		a,b,c =  b+c,2*c+b,3*c+2*b
		# I've compressed all the steps of moving forward on the sequence, every 3rd item is even so 'a' is ALWAYS even.
	return total
