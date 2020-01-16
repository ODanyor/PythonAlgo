import random as rd
from math import sqrt

def main():
	def amount_of_points(amount):
		points_in_cycle = 0
		points_in_total = 0
		initial_progress = 0
		for n in range(amount):
			x_coordinate = rd.uniform(0, 1)
			y_coordinate = rd.uniform(0, 1)
			point_location = float(sqrt(x_coordinate**2 + y_coordinate**2))

			progress = (n*100)/amount
			if int(initial_progress) != int(progress):
				print(f"Completed: {int(progress)}%")
			initial_progress = progress


			if point_location <= 1:
				points_in_cycle += 1
			points_in_total += 1

		pi = 4*(points_in_cycle/points_in_total)
		print("Completed 100%")
		print(pi)
	amount_of_points(1000000)

if __name__ == "__main__":
	main()

