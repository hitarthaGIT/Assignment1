# If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

print("Hello World !")

#output : Hello World !

print("Hello world !)
      
#Output: SyntaxError: unterminated string literal (detected at line 7)
      
print(Hello World !)

#Output : SyntaxError: invalid syntax. Perhaps you forgot a comma?