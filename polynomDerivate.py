# Input
many = int(input("How big polynom: "))+1

FX = []
fx = []
for i in range(many,0,-1):
	FX.append(int(input(str(i-1)+"'s x: ")))

# Main derivation
for i in range(many-1):
	fx.append((many-i-1)*FX[i])

# Output
print()
for i in range(len(fx)-1,0,-1):
	if fx[many-i-2] != 0:
		print(str(fx[many-i-2])+"x^"+str(i)+" + ",end='')

if fx[many-2] != 0:
	print(str(fx[many-2]))
else:
	print()
