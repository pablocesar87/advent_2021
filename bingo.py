import pandas as pd
import sys

from functools import partial


COLUMNS = list("ABCDE")


class Carton:
	def __init__(self, carton_df):
		self.carton_df = carton_df
		self.picked = pd.DataFrame([[False] * 5 for _ in range(5)], columns=COLUMNS)

	def check_new_number(self, number):
		for column in COLUMNS:
			if not self.carton_df[self.carton_df[column] == number].empty:
				self._mark_picked_number(column, self.carton_df[self.carton_df[column] == number].index)

	def _mark_picked_number(self, column, index):
		self.picked[column].iloc[index] = True


	def check_winner_carton(self):
		for column in COLUMNS:
			if self.picked[column].all():
				return True
		for row in self.picked.index:
			if self.picked.iloc[row].all():
				return True
		return False

	def get_final_score(self, winner_number):
		# suma todos los que son false
		# multiplica por el numero que ha hecho ganar
		def _apply(self, column, row):
			for index, value in enumerate(row):
				if self.picked[column][index]:
					self.carton_df[column][index] = 0

		for column in COLUMNS:
			self.carton_df.apply(partial(_apply, self, column))
		return self.carton_df.values.sum() * winner_number


def play():
	# prepare the bingo
	bingo_cartons = []
	bingo_cartons_objects = []

	with open("bingo_input.txt", "r") as bingo_input:
		for index, value in enumerate(bingo_input):
			if index == 0:
				bingo_numbers = value.strip().split(",")
			elif index > 1:
				row = value.strip().replace("  ", " ").split(" ")
				if len(row) != 5:
					continue
				bingo_cartons.append(row)
				if len(bingo_cartons) == 5:
					carton_df = pd.DataFrame(bingo_cartons, columns=COLUMNS)
					for column in COLUMNS:
						carton_df[column] = pd.to_numeric(carton_df[column])
					bingo_cartons_objects.append(Carton(carton_df))
					bingo_cartons = []

	# play the bingo
	for new_number in bingo_numbers:
		for carton in bingo_cartons_objects:
			carton.check_new_number(int(new_number))
			if carton.check_winner_carton():
				print("The final score is: {}".format(carton.get_final_score(int(new_number))))
				sys.exit(1)


if __name__ == "__main__":
    play()