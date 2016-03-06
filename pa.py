def getHammingDistance(str1, str2):
	#checks if string1 is a string
	if(isinstance(str1, str)):
		str1Len = len(str1)
		if(str1Len == 0):
			return "Error! Invalid first string"
	else:
		return "Error! First string is not a string"
		
	#checks if string2 is a string
	if(isinstance(str2, str)):	
		str2Len = len(str2)	
		if(str2Len == 0):
			return "Error! Invalid second string"
	else:
		return "Error! Second string is not a string"
		
	#for indexing and counting the number of different character
	index = 0
	counter = 0
	
	#checks if both strings have the same length
	if(str1Len != str2Len):
		return "Error! Strings are not equal!"		
		
	#traverses both strings and checks each character
	for c in str1:
		if c == str2[index]:
			index = index + 1
		else:
			counter = counter + 1
			index = index + 1
	return counter

def countSubstrPattern(original, pattern):
	#checks if original is a string
	if(isinstance(original, str)):
		originalLen = len(original)
		if(originalLen == 0):
			return "Error! Invalid string to traverse"
	else:
		return "Error! String to traverse is not a string"
		
	#checks if pattern is a string
	if(isinstance(pattern, str)):	
		patternLen = len(pattern)	
		if(patternLen == 0):
			return "Error! Invalid pattern string"
	else:
		return "Error! Pattern string is not a string"

	counter = 0 #for counting the number of substring pattern found
	newbeg = 0 #for moving through the string, index
	
	while(newbeg <= len(original)):	
		#if substring is not found
		if(original.find(pattern, newbeg, newbeg + len(pattern)) == -1):
			newbeg = newbeg + 1
		#else substring is found
		else:
			counter = counter + 1
			newbeg = newbeg + 1
	return counter

def isValidString(string, alphabet):
	#checks if string is a string
	if(isinstance(string, str)):
		strLen = len(string)
		if(strLen == 0):
			return "Error! Invalid string to traverse"
	else:
		return "Error! String to traverse is not a string"
		
	#checks if alphabet is a string
	if(isinstance(alphabet, str)):	
		alphabetLen = len(alphabet)	
		if(alphabetLen == 0):
			return "Error! Invalid pattern string"
	else:
		return "Error! Pattern string is not a string"

	#boolean variable
	checker	= None
	
	#checks each character in the given string with each character in the given alphabet
	for char in string:
		#resets the value of checker
		checker = False
		for alphabetChar in alphabet:
			#if already found a match, breaks with the current loop
			if(char == alphabetChar ):
				checker = True
				break
		#if checker is not changed, returns false
		if(checker == False):
			return checker
	#for returning true			
	return checker
	

def getSkew(string, n):
	#checks if string is a string
	if(isinstance(string, str)):
		strLen = len(string)
		if(strLen == 0):
			return "Error! Invalid string to traverse"
	else:
		return "Error! String to traverse is not a string"
		
	#checks if n is an int
	if(isinstance(n, int)):	
		if(n <= 0 or n > strLen):
			return "Error! Invalid n"
	else:
		return "Error! N is not valid"
		
	string.upper() #converts the string to uppercase
	gCount = string.count("G", 0, n) #counts the number of G with the substring from 0 to n
	cCount = string.count("C", 0, n) #counts the number of C with the substring from 0 to n
	
	difference = gCount - cCount
	
	return difference


def getMaxSkewN(string, n):
	#checks if string is a string
	if(isinstance(string, str)):
		strLen = len(string)
		if(strLen == 0):
			return "Error! Invalid string to traverse"
	else:
		return "Error! String to traverse is not a string"
		
	#checks if n is an int
	if(isinstance(n, int)):	
		if(n <= 0 or n > strLen):
			return "Error! Invalid n"
	else:
		return "Error! N is not valid"

	#variables for looping and getting the difference
	counter = 1
	difference = 0	
	
	while(counter <= n):
		newDifference = getSkew(string, counter)	#gets the skew of the string with current n
		if(newDifference > difference):					#if the result is larger, stores the result
			difference = newDifference
		counter = counter + 1
	
	return difference

def getMinSkewN(string, n):	
	#checks if string is a string
	if(isinstance(string, str)):
		strLen = len(string)
		if(strLen == 0):
			return "Error! Invalid string to traverse"
	else:
		return "Error! String to traverse is not a string"
		
	#checks if n is an int
	if(isinstance(n, int)):	
		if(n <= 0 or n > strLen):
			return "Error! Invalid n"
	else:
		return "Error! N is not valid"

	#variables for looping and getting the difference
	counter = 1
	difference = getSkew(string, counter)	#initialize differences with the first skew
	
	while(counter <= n):
		newDifference = getSkew(string, counter)	#gets the skew of the string with current n
		if(newDifference < difference):					#if the result is smaller, stores the result
			difference = newDifference
		counter = counter + 1
	
	return difference
	