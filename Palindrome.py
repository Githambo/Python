string=str(input("Enter a string\n"))

def ReverseFunction(string):
	return string[::-1]


def PalindromeCheck(string):
	rev=ReverseFunction(string)
	print("original string is -->",string)
	print("Reversed string is -->",rev)

	
	if rev==string:
		print(string,"is a palindrome")
	else:
		print(string,"is not a palindrome")

		

print(PalindromeCheck(string))
