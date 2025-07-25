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
				print("Amount must be greater than zero!")
		else:
			print("Enter a number!")

	return amount

def num_of_lines():
	while True:
		lines = input("How many rows you wanna bet on(1-" + str(	MAX_LINES) + "): ")
		if lines.isdigit():
			lines = int(lines)
			if MAX_LINES >= lines >= MIN_LINES:
				break
			else:
				print("This row is not available. Try again!") 
		else:
			print("Enter a number!")

	return lines

def get_bet():
	while True:
		amount = input("Enter the bet amount: ")
		if amount.isdigit():
			amount = int(amount)
			if MAX_BET >= amount >= MIN_BET:
				break
			else:
				print(f"Amount must be between {MAX_BET} and {MIN_BET}")
	return amount

symbol_count = { "A": 9, "B": 15, "C": 25, "D": 30 }
symbol_value = {"A": 8, "B": 6, "C": 4, "D": 2}

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

def check_winnings(columns, lines, bet, values):
	winnings = 0
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_to_compare = column[line]
			if symbol != symbol_to_compare:
				break
		else:
			winnings += values[symbol] * bet

	return winnings

def spin():

	balance= deposit()

	while True:

		lines = num_of_lines()
		bet = get_bet()
		total_bet = bet * lines
		balance -= total_bet

		print(f"Your total bet amount: {total_bet}.")
		print()
		print(f"Your remaining balance: {balance}")
		print()

		slots = slot_machine_spin(ROWS, COLS, symbol_count)
		print_spin(slots)
		print()

		winnings = check_winnings(slots, lines, bet, symbol_value)
		print(f"You won {winnings}")
		balance += winnings
		print(f"Your new balance is: {balance}")

		answer = input("Press Enter to play again OR Press 'q' to quit. ")
		if answer == 'q':
			break

		if balance < 20:
			print("You do not have enough balance to play. Deposit again!")
			print(f"Current balance: {balance}")
			break
 

def main():

	spin()

main()
