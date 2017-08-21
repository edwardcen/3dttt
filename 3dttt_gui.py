from tkinter import *
from game_structure import *

# Draw message needs fixing


class Game():

	player_one_highlight_color = "#87CEEB" # Sky Blue
	player_one_clicked_color = "#4169E1" # Royal Blue

	player_two_highlight_color = "#FFB6C1" # Light Pink
	player_two_clicked_color = "#EE1304" # Rouge Red

	line_coordinates = [
	[0, 225, 450, 225, 10],
	[225, 0, 225, 450, 10],
	[56, 234, 56, 446, 4],
	[110, 234, 110, 446, 4],
	[164, 234, 164, 446, 4],
	[286, 234, 286, 446, 4],
	[340, 234, 340, 446, 4],
	[394, 234, 394, 446, 4],
	[56, 4, 56, 216, 4],
	[110, 4, 110, 216, 4],
	[164, 4, 164, 216, 4],
	[286, 4, 286, 216, 4],
	[340, 4, 340, 216, 4],
	[394, 4, 394, 216, 4],
	[234, 56, 446, 56, 4],
	[234, 110, 446, 110, 4],
	[234, 164, 446, 164, 4],
	[234, 286, 446, 286, 4],
	[234, 340, 446, 340, 4],
	[234, 394, 446, 394, 4],
	[4, 56, 216, 56, 4],
	[4, 110, 216, 110, 4],
	[4, 164, 216, 164, 4],
	[4, 286, 216, 286, 4],
	[4, 340, 216, 340, 4],
	[4, 394, 216, 394, 4]]

	square_coordinates = [29, 83, 137, 191, 259, 313, 367, 421]

	def __init__(self):
		self.master = Tk()
		self.buttons = []
		self.player_one_name = StringVar()
		self.player_two_name = StringVar()
		self.draw_window()
		self.draw_board()
		self.draw_menu()
		self.master.mainloop()


	def draw_window(self):
		self.master.title("3D Tic Tac Toe")
		self.header_frame = Frame(self.master, height = 28, width = 450)
		self.header_frame.grid(row = 0, column = 0)
		self.header_frame.grid_propagate(0)
		self.start_button = Button(self.header_frame, text = "Start Game", command = self.game_info_command	)
		self.start_button.pack()
		self.game_frame = Frame(self.master, height = 450, width = 450)
		self.game_frame.grid(row = 1, column = 0)
		self.game_frame.grid_propagate(0)
		self.game_canvas = Canvas(self.game_frame, height = 450, width = 450, bg = "white")
		self.game_canvas.grid()



	def draw_board(self):
		for coordinates in Game.line_coordinates:
			self.game_canvas.create_line(coordinates[0],coordinates[1],coordinates[2], coordinates[3], width = coordinates[4], capstyle = ROUND)
		self.game_canvas.create_text(50, 225, fill = "white", text = "Square One \u2191")
		self.game_canvas.create_text(165, 225, fill = "white", text = "Square Three \u2193")
		self.game_canvas.create_text(275, 225, fill = "white", text = "Square Two \u2191")
		self.game_canvas.create_text(400, 225, fill = "white", text = "Square Four \u2193")	

	def draw_squares(self):
		for xcoord in Game.square_coordinates:
			for ycoord in Game.square_coordinates:
				self.buttons += [Square(xcoord, ycoord, self)]		


	def draw_menu(self):
		self.menubar = Menu(self.master)
		self.game_menu = Menu(self.menubar, tearoff = 0)
		self.game_menu.add_command(label = "Start Game", command = self.game_info_command)
		self.game_menu.add_command(label = "Settings", command = self.settings_command)
		self.help_menu = Menu(self.menubar, tearoff = 0)
		self.help_menu.add_command(label = "Instructions", command = self.instructions_command)
		self.help_menu.add_command(label = "Acknowledgements", command = self.acknowledgements_command)
		self.menubar.add_cascade(label = "Game", menu = self.game_menu)
		self.menubar.add_cascade(label = "Help", menu = self.help_menu)
		self.menubar.add_command(label = "Quit", command = self.master.quit)
		self.master.config(menu = self.menubar)

	def help_command(self):
		return None

	def game_info_command(self):
		self.name_input = Toplevel(takefocus = True)
		self.name_input.lift()
		Label(self.name_input, text = "Enter First Player Name: ").grid(row = 0, column = 0)
		Entry(self.name_input, textvariable = self.player_one_name, width = 15).grid(row = 0, column = 1)
		Label(self.name_input, text = "Enter Second Player Name: ").grid(row = 1, column = 0)
		Entry(self.name_input, textvariable = self.player_two_name, width = 15).grid(row = 1, column = 1)
		Button(self.name_input, text = "Done", command = self.start_game_command).grid(row = 0, rowspan = 2, column = 2)


	def acknowledgements_command(self):
		return None

	def settings_command(self):
		return None

	def instructions_command(self):
		return None

	def start_game_command(self):
		self.name_input.withdraw()
		self.players = [Player(self.player_one_name.get(), 1 , "X",[Game.player_one_highlight_color, Game.player_one_clicked_color])] + [Player(self.player_two_name.get(), -1 , "O", [Game.player_two_highlight_color, Game.player_two_clicked_color])]
		self.board = GameBoard(self.players)
		self.start_button.destroy()
		self.draw_squares()
		self.draw_message()

	def draw_message(self):
		try:
			self.message.config(text = "{}'s Turn".format(self.board.current_player.name), bg = self.board.current_player.colors[0])
		except AttributeError:
			self.message = Label(self.header_frame, width = 55, pady = 5, text = "{}'s Turn".format(self.board.current_player.name), bg = self.board.current_player.colors[0]) 
			self.message.pack()

	def clicked(self, location):
		self.board.take_move(location)
		if self.board.win_condition():
			self.board.other()
			self.message.config(text = "{} Won!".format(self.board.current_player.name), bg = self.board.current_player.colors[1])
			for square in self.buttons:
				square.button.config(state = DISABLED)
		else:
			self.draw_message()
			for square in self.buttons:
				square.button.config(activebackground = self.board.current_player.colors[0])


class Square():
	def __init__(self, xcoord, ycoord, game):
		self.game = game
		self.button = Button(self.game.game_canvas, bitmap = "gray50",relief = FLAT, overrelief = FLAT, bd = 0, width = 46, height = 46, bg = "white", activebackground = self.game.board.current_player.colors[0], command = self.click)
		self.official_id = self.game.game_canvas.create_window(xcoord, ycoord, window = self.button)
		self.issue_location(xcoord, ycoord)

	def click(self):
		self.button.config( bg = self.game.board.current_player.colors[1])
		self.button.config(state = DISABLED)
		self.game.clicked(self.placement)



	def issue_location(self, xcoord, ycoord):
		if xcoord < 200 and ycoord < 200:
			self.placement = [0]

		elif xcoord < 200 and ycoord > 200:
			self.placement = [2]

		elif xcoord > 200 and ycoord < 200:
			self.placement = [1]

		elif xcoord > 200 and ycoord > 200:
			self.placement = [3]

		if xcoord == 29 or xcoord == 259:
			self.placement += [0]
		elif xcoord == 83 or xcoord == 313:
			self.placement += [1]
		elif xcoord == 137 or xcoord == 367:
			self.placement += [2]
		elif xcoord == 191 or xcoord == 421:
			self.placement += [3]

		if ycoord == 29 or ycoord == 259:
			self.placement += [0]
		elif ycoord == 83 or ycoord == 313:
			self.placement += [1]
		elif ycoord ==137 or ycoord == 367:
			self.placement += [2]
		elif ycoord == 191 or ycoord == 421:
			self.placement += [3]		


placeholder = Game()