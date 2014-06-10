import sys
"""
http://en.wikipedia.org/wiki/Brainfuck
> 	increment the data pointer (to point to the next cell to the right).
< 	decrement the data pointer (to point to the next cell to the left).
+ 	increment (increase by one) the byte at the data pointer.
- 	decrement (decrease by one) the byte at the data pointer.
. 	output the byte at the data pointer.
, 	accept one byte of input, storing its value in the byte at the data pointer.
[ 	if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
] 	if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
"""

def runBF(program="Nothing"):

	data = bytearray(4)
	ptrstack = []
	data_i = 0
	index = 0

	# If we were not passed a program then ask the user to give us one.
	if program == "Nothing":
		program = raw_input("Input Program:")

	#Process Program
	while index < len(program):

		if program[index] == ">": # Increment Data Pointer
			data_i += 1
			if data_i == len(data):
				data.append(0)
		elif program[index] == "<":# Decrement Data Pointer
			if data_i == 0: #Check to see if we've rolled out of the data array
				data.insert(0,0)
			else:
				data_i -= 1
		elif program[index] == "+":# Increment byte at pointer
			try:
				data[data_i] = data[data_i] + 1
			except ValueError: #Roll over on fail.
				data[data_i] = 0

		elif program[index] == "-":# Decrement byte at pointer
			try:
				data[data_i] = data[data_i] - 1
			except ValueError: #Roll Over on fail.
				data[data_i] = 255
		elif program[index] == '.':# Print data
			sys.stdout.write(chr(data[data_i]))
		elif program[index] == ',':
			data[data_i] = sys.stdin.read(1)
			sys.stdin.read(1)
		elif program[index] == '[':
			# WHILE LOOP START!
			if data[data_i] == 0:
				index = data.find("]",index)
				if index == -1:
					return "Error: Unbalanced Brackets"
			else:
				ptrstack.append(index)	
		elif program[index] == ']': # WHILE LOOP END!
				if data[data_i] != 0: 
					index = ptrstack[-1]
				else:
					ptrstack.pop() # Get rid of the pointer we no longer need it!
		index += 1

import random
"""
What is expected:
	This program must never crash
	This program must return instead of print.
	This program will have infinite loop protection.			
"""
def runBF_web(program):
# FIX ME

	data = bytearray(4)
	ptrstack = []
	data_i = 0
	index = 0
	steps = 0
	output = ""
	maximum_steps = 100000

	# If we were not passed a program then return
	if type(program) != str: 
		return "Error: No Program found OR program has an invalid type."

	#Process Program
	while index < len(program) and steps < maximum_steps:

		if program[index] == ">": # Increment Data Pointer
			data_i += 1
			if data_i == len(data):
				data.append(0)
		elif program[index] == "<":# Decrement Data Pointer
			if data_i == 0: #Check to see if we've rolled out of the data array
				data.insert(0,0)
			else:
				data_i -= 1
		elif program[index] == "+":# Increment byte at pointer
			try:
				data[data_i] = data[data_i] + 1
			except ValueError: #Roll over on fail.
				data[data_i] = 0

		elif program[index] == "-":# Decrement byte at pointer
			try:
				data[data_i] = data[data_i] - 1
			except ValueError: #Roll Over on fail.
				data[data_i] = 255
		elif program[index] == '.':# Print data
			output += chr(data[data_i])
		elif program[index] == ',':
			data[data_i] = random.randint(0,255)
		elif program[index] == '[':
			# WHILE LOOP START!
			if data[data_i] == 0:
				index = program.find("]",index)
				if index == -1: # Check if the User entered an invalid program.
					return output + "\n" + "Error: Unbalanced Brackets" 
				#if ptrstack == [] or ptrstack[-1] != index: # Ensure that the we don't throw an exception if the loop is kicked out before it runs once.
				#	ptrstack.append(index)
					
			else:
				ptrstack.append(index)	
		elif program[index] == ']': # WHILE LOOP END!
				try: # We can't have the program explode the webpage so we'll have error handling here.
					if data[data_i] != 0: 
						index = ptrstack[-1]
					else:
						ptrstack.pop() # Get rid of the pointer we no longer need it!
				except:
					return output + "\n" + "Error: Unbalanced Brackets"
		index += 1
		steps += 1
	if steps == maximum_steps: # Check to see if we flash a warning that we timed out.
		return output + "\n" + "Error: Maximum iterations reached [{}]".format(maximum_steps) 
	return output