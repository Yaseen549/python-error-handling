

def filter_vowels():
	newString = input("Enter your string: ")
	vowels = ('a','e','i','o','u','A','E','I','O','U')
	for x in newString.lower():
		if x in vowels:
			newString = newString.replace(x,"")
	return newString

def filter_constants():
	constants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
	return ''.join(c for c in newString if c.lower() not in constants)
	
