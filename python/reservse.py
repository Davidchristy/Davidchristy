string = input()
newStr = ""
for i in string.split():
	# print(i)
	for j in range(0, -len(i), -1):
		# print(j)
		newStr += i[j-1]
	newStr += " "
	# print(i)
newStr = newStr[:-1]
print(newStr)
