user_input = input("camelCase :")
print ("snake_case: ", end="")
for c in user_input:
    if c.islower() :
      print(c, end="")
    if c.isupper() :
      print("_", end="")
      print(c.lower(), end="")

print()

