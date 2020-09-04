import random

nums = []

for i in range(0, random.randint(50, 101)):
	nums.append(random.randint(0, 1000))

print(min(nums))
print(nums.index(min(nums)))
