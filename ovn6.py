import random

nums = []

for i in range(0, random.randint(50, 101)):
	nums.append(random.randint(0, 1000))

result = []

while nums:
	min_num = min(nums)
	index = nums.index(min(nums))

	nums.pop(index)
	result.append(min_num)

result

print(result)
