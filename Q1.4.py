#In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?

# let's consider adding two numbers containg leading 0's:

res=09+011
print(res)

# Output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers