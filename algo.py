import random
import time

base = [[], [], []]
def main():
	# First step
	time1 = 0
	time2 = 0
	timeH = [time1, time2]
	for n in range(1, 3):
		for n2 in range(1, 11):
			t = random.uniform(.1, 3.9)
			time.sleep(t)
			num = random.randint(
			10000000000000000000,
			99999999999999999999)
			base[n-1].append(num)
			print(f"Algorithm: {num}")
			timeH[n-1] += t
		print(f'Base {n}: {len(base[n-1])}')
		print(f"Overall time of {n} pair: {timeH[n-1]}s")
	base[2] = base[0]+base[1]
	print(len(base[2]))

	# Second step
	time3 = timeH[0]+timeH[1]
	for n in range(1, len(base[2])):
		t = random.uniform(.1, 3.9)
		time.sleep(t)
		time3 += t
		print(f"Algorithm: {base[2][n-1]}")
	# Third step
	print(f"Pairing of 1 and 2 sets has been completed in {time3}s")
	

if __name__ == '__main__':
	main()
