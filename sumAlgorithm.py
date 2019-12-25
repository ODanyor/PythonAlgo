numbers = [1, 9, 2, 4] #summury of pairs equal to expected number
def sumAlgorithm(numbers, expectedNum):
	def sum_of_pairs(a, b):
		sum = a+b
		if sum == expectedNum:
			print(f"{sum}={a}+{b}")
		else: pass

	def matcher(numbers, signX, signY):
		for x in list(numbers):
			counter=0
			for y in list(numbers):
				if x == y:
					pass
				else:
					x = x*signX
					y = y*signY
					sum_of_pairs(x, y)

	for n in range(1, 4):
		if n == 1:
			signX = 1
			signY = 1
			matcher(numbers, signX, signY)
		elif n == 2:
			signX = -1
			signY = 1
			matcher(numbers, signX, signY)
		elif n == 3:
			signX = 1
			signY = -1
			matcher(numbers, signX, signY)
if __name__ == '__main__':
	sumAlgorithm(numbers, 7)