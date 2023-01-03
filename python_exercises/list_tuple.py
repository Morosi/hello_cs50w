list = []
tupl = ()
while len(list) < 5:
    list.append(int(input("enter a number: ")))
print(list)

while len(tupl) < 5:
    tupl = tupl + tuple(input("Enter a number:"))

print(tupl)

new_tupl = tupl + ('', '', '1', '2', '0', '')

print("")
print(new_tupl)

    

