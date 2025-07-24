import random

MAX_LINES = 3
MIN_LINES = 1

MAX_BET = 1000
MIN_BET = 20

ROWS = 3
COLS = 3

def deposit():
	while True:
		amount = input("What amount you wanna deposit? ")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				break
			else:
				print("amount must be greater than zero!")
		else:
			print("enter a number!")

	return amount

def num_of_lines():
	while True:
		lines = input("enter the number of lines (1-" + str(	MAX_LINES) + ") ")
		if lines.isdigit():
			lines = int(lines)
			if MAX_LINES >= lines >= MIN_LINES:
				break
			else:
				print("enter a valid number of lines!") 
		else:
			print("enter a number!")

	return lines

def get_bet():
	while True:
		amount = input("enter the bet amount: ")
		if amount.isdigit():
			amount = int(amount)
			if MAX_BET >= amount >= MIN_BET:
				break
			else:
				print(f"amount must be between {MAX_BET} and {MIN_BET}")
	return amount

symbol_count = { "A": 2, "B":4, "C":6, "D":8 }

def slot_machine_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)

	columns = []		
	for col in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for row in range(rows):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)

		columns.append(column)

	return columns

def print_spin(columns):
	for row in range(len(columns[1])):
		for i, column in enumerate(columns):
			if i != len(columns)-1 :
				print(column[row], end=" | ")
			else:
				print(column[row], end="")

		print()


def main():
	deposit_amt = deposit()
	lines = num_of_lines()
	bet = get_bet()
	total_bet = bet * lines
	balance = deposit_amt - int(total_bet)

	slots = slot_machine_spin(ROWS, COLS, symbol_count)
	print_spin(slots)

	"""print(balance, lines)
	print(total_bet)"""

main()
