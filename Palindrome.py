#Palindrome.py By Kenneth Githambo 
#palindrome is a string that when reversed its still the same 


string=str(input("Enter a string\n")) 

def ReverseFunction(string):#this function reverses the string charcters 
	return string[::-1]

def PalindromeCheck(string):#This fucntion compares the rerversed string with the original String
	rev=ReverseFunction(string)
	print("original string is -->",string)
	print("Reversed string is -->",rev)
	
	if rev==string:
		print(string,"is a palindrome")
	else:
		print(string,"is not a palindrome")		

print(PalindromeCheck(string))
