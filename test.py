def sort_numbers(numbers):
	"""使用冒泡排序将数字列表按升序排列。"""
	result = numbers.copy()
	for i in range(len(result)):
		for j in range(len(result) - 1 - i):
			if result[j] > result[j + 1]:
				result[j], result[j + 1] = result[j + 1], result[j]
	return result


if __name__ == "__main__":
	print(sort_numbers([5, 2, 8, 1, 3]))
