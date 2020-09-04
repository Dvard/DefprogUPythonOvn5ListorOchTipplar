amount = int(input('Hur många tal: '))

numbers = []

for i in range(0, amount):
	numbers.append(int(input('Tal: ')))

for num in numbers[::-1]:
	print(num)
