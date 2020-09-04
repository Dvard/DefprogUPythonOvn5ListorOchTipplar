amount = int(input('Hur många tal: '))

numbers = []

for i in range(0, amount):
	numbers.append(int(input('Tal: ')))

total_sum = 0

median = 0

for num in numbers:
	total_sum += num
	print(abs(num))

median = total_sum / len(numbers)


print(total_sum)
print(median)
