import random

def run(program, maximum_steps=1000000):
	data = bytearray(4)
	ptrstack = []
	data_i = 0
	index = 0
	steps = 0
	output = ""

	# If we were not passed a program then return
	"""if type(program) != str:
		output += str(type(program))
		program = str(program)"""

	#Process Program
	while index < len(program) and steps < maximum_steps:

		if program[index] == u">": # Increment Data Pointer
			data_i += 1
			if data_i == len(data):
				data.append(0)
		elif program[index] == u"<":# Decrement Data Pointer
			if data_i == 0: #Check to see if we've rolled out of the data array
				data.insert(0,0)
			else:
				data_i -= 1
		elif program[index] == u"+":# Increment byte at pointer
			try:
				data[data_i] = data[data_i] + 1
			except ValueError: #Roll over on fail.
				data[data_i] = 0

		elif program[index] == u"-":# Decrement byte at pointer
			try:
				data[data_i] = data[data_i] - 1
			except ValueError: #Roll Over on fail.
				data[data_i] = 255
		elif program[index] == u'.':# Print data
			output += chr(data[data_i])
		elif program[index] == u',':
			data[data_i] = random.randint(0,255)
		elif program[index] == u'[':
			# WHILE LOOP START!
			if data[data_i] == 0:
				index = program.find("]",index)
				if index == -1: # Check if the User entered an invalid program.
					return output + "\n" + "Error: Unbalanced Brackets"
				#if ptrstack == [] or ptrstack[-1] != index: # Ensure that the we don't throw an exception if the loop is kicked out before it runs once.
				#	ptrstack.append(index)

			else:
				ptrstack.append(index)
		elif program[index] == u']': # WHILE LOOP END!
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