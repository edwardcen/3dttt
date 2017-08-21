"""
This is the game structure for 3D Tic Tac Toe.
I will use classes to create the game board, with 2 classes.
One will be the 2D 4x4 board, the other, 4 of them stacked together

Created by Edward Cen
"""
class GameBoard():

	def __init__(self, players):
		assert type(players) == list, "Not a list"
		assert len(players) == 2, "Incorrect dimensions"
		assert isinstance(players[0],Player), "Must be Player objects"

		self.state=[Flatboard() for _ in range(4)]
		self.players = players
		self.current_player = players[0]

	# switches whatever player is currently active
	def other(self):
		if self.current_player == self.players[0]:
			self.current_player = self.players[1]
		else:
			self.current_player = self.players[0]

	def take_move(self, place):
		assert type(place) == list, "Not a list"
		assert len(place) == 3, "Incorrect dimensions"
		assert type(place[0]) == int, "Dimensions must be integers"
		assert type(place[1]) == int, "Dimensions must be integers"
		assert type(place[2]) == int, "Dimensions must be integers"
		assert place[0] <= 3, "Out of box (First dimension too big)"
		assert place[0] >= 0, "Out of box (First dimension too small)"
		assert place[1] <= 3, "Out of box (Second dimension too big)"
		assert place[1] >= 0, "Out of box (Second dimension too small)"
		assert place[2] <= 3, "Out of box (Third dimension too big)"
		assert place[2] >= 0, "Out of box (Third dimension too small)"

		board_to_play = self.state[place[0]]
		board_to_play.take_move(place[1:], self.current_player)
		self.other()

	def win_condition(self):
		# Checks for wins in each of the 2D boxes
		for flatboard in self.state:
			if flatboard.win_condition() == True:
				return True
		# Checks for wins in each position across the 4 stacks
		for xcoord in range(4):
			for ycoord in range(4):
				total = 0
				for flatboard in self.state:
					total += flatboard.state[xcoord][ycoord]
				if abs(total) == 4:
					return True

		# Checks for horizontal-diagonal wins across stacks
		for row in range(4):
			total = 0
			for position in range(4):
				total += self.state[position].state[row][position]
			if abs(total) == 4:
				return True

		for row in range(4):
			total = 0
			for position in range(4):
				total += self.state[position].state[row][3 - position]
			if abs(total) == 4:
				return True
		# Checks for vertical-diagonal wins across stacks
		for column in range(4):
			total = 0
			for position in range(4):
				total += self.state[position].state[position][column]
			if abs(total) == 4:
				return True

		for row in range(4):
			total = 0
			for position in range(4):
				total += self.state[position].state[3 - position][column]
			if abs(total) == 4:
				return True
		# Checks for the 4 diagonal wins that connect the 8 corners
		total1, total2, total3, total4 = 0, 0, 0, 0
		"""for xcoord in range(4):
			for ycoord in range(4):
				for zcoord in range(4):
					total1 += self.state[xcoord].state[ycoord][zcoord]
					total2 += self.state[3-xcoord].state[ycoord][zcoord]
					total3 += self.state[xcoord].state[3-ycoord][zcoord]
					total4 += self.state[xcoord].state[ycoord][3-zcoord]
		"""
		for coord in range(4):
			total1 += self.state[coord].state[coord][coord]
			total2 += self.state[3-coord].state[coord][coord]
			total3 += self.state[coord].state[3-coord][coord]
			total4 += self.state[coord].state[coord][3-coord]
		if abs(total1) == 4 or abs(total2) == 4 or abs(total3) == 4 or abs(total4) ==  4:
			return True
		# If none add up to abs(4), return False
		return False		

	def __repr__(self):
		string = ""
		for board in self.state:
			string += str(board) + "\n"
		return string

	def generate_nested_list(self):
		nested_list = []
		for flatboard in self.state:
			nested_list += [flatboard.state]
		return nested_list




class Flatboard():

	# The flat board will be represented by a 4x4 nested list, with 0 as the base value
	def __init__(self):
		self.state = [[0 for _ in range(4)] for _ in range(4)]
		self.text = [["-" for _ in range(4)] for _ in range(4)]

	# Place will be a [x,y] coordinate.
	# x will represent the row, and y the column
	# It will check if the coordinate has already been played, if it has, raise error
	# Else, it will change the coordinate value to either 1 or -1, for Player1 and Player2 respectively

	def take_move(self, place, player):
		# All assertions should've been made in the call of Gameboard
		point = self.state[place[0]][place[1]]
		if point == 0:
			self.state[place[0]][place[1]] = player.value
			self.text[place[0]][place[1]] = player.character
		else:
			raise AssertionError("Place already occupied")

	def win_condition(self):
		# Checks for horizontal wins
		for line in self.state:
			if abs(sum(line)) == 4:
				return True
		# Checks for vertical wins
		for column in range(4):
			total = 0
			for line in self.state:
				total += line[column]
			if abs(total) == 4:
				return True
		# Checks for left to right diagonal win
		total = 0
		for position in range(4):
			total += self.state[position][position]
		if abs(total) == 4:
			return True
		#Checks for right to left diagonal win
		total = 0
		for position in range(4):
			total += self.state[3-position][position]
		if abs(total) == 4:
			return True
		#If none are True, return False
		return False

	def __repr__(self):
		string = ""
		for line in self.text:
			for elem in line:
				string += str(elem) + " "
			string += "\n"
		return string
			
class Player():
	def __init__(self, name, value, char, colors):
		self.name = name
		self.value = value
		self.character = char
		self.colors = colors

def play_game():
	players = []
	print("Welcome to 3D Tic Tac Toe")
	player1 = input("What is the first player's name?\n")
	player2 = input("What is the second player's name?\n")
	players = [Player(player1, 1 , "X")] + [Player(player2, -1 , "O")]
	board = GameBoard(players)
	while True:
		if board.win_condition():
			board.other()
			print("{0} wins!".format(board.current_player.name))
			return
		print()
		try:
			name = board.current_player.name
			string_coordinate = input("It is {0}'s turn. Please select an available square.\n".format(name)) #input is a [x,y,z] list
			coordinate = [int(string_coordinate[1])] + [int(string_coordinate[3])] + [int(string_coordinate[5])]
			board.take_move(coordinate)
			print(board)
		except AssertionError as e:
			print(e)
			print("Try again!")

		except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
			print('\nGood game. Bye!')
			return

"""		
This is the code that runs when the file is executed, it will start the game with a clean board, starting with player 1
"""
# play_game()
A = Player("Player1", 1, "X", "blue")
B = Player("Player2", -1, "O", "red")
G = GameBoard([A, B])