# Given an array of integers, find the most friquent integers from the list
# Write a method that returns frequent integer

def main():
	def frequentInteger(arr, l):
		arr.sort()
		# [1, 1, 1, 2, 2, 4, 4, 5, 9, 9, 9, 9]
		max_count = 1; res = arr[0]; curr_count = 1

		for i in range(0, l):
			if arr[i] == arr[i-1]:
				curr_count += 1
			else:
				if (curr_count > max_count):
					max_count = curr_count
					res = arr[i-1]
				curr_count = 1

		if (curr_count > max_count):
			max_count = curr_count
			res = arr[i]
			
		return res

	integers = [1, 2, 4, 9, 5, 2, 1, 4, 1, 9, 9, 9]
	length = len(integers)
	print(frequentInteger(integers, length))

if __name__ == "__main__":
	main()