expression = input("Expression: ")
parts = expression.split()
x = float(parts[0])
z = float(parts[2])
op= parts[1]
if op == "+":
    print(f"{x + z:.1f}")
elif op == "-":
    print( f"{x - z:.1f}")
elif op == "/":
    print (f"{x / z:.1f}" )
elif op == "*":
    print ( f"{x * z:.1f}" )
