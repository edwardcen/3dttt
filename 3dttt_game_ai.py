from copy import *
from game_structure import *


class GameTree():
	def __init__(self, initial_state, initial_player_value, target_depth, depth = 0):
		self.value = initial_player_value
		self.state = []
		self.branches = []
		if depth < target_depth:
			self.generate_moves(initial_state, target_depth, depth)
		else:
			self.state = initial_state

	def generate_moves(self, initial_state, target_depth, depth):
		for x in range(len(initial_state)):
			for y in range(len(initial_state)):
				for z in range(len(initial_state)):
					if initial_state[x][y][z] == 0:
						state = deepcopy(initial_state)
						state[x][y][z] = self.value
						branch = GameTree(state, -1 * self.value, target_depth, depth + 1)
						self.branches += [branch]

	def __repr__(self):
		string = ""
		if self.state:
			string += str(self.state)
			return string
		else:
			for branch in self.branches:
				string += str(branch)
			return string







class Bot():
	parameters = []
	def __init__(self):
		return None




class MiniMaxTree():
	def __init__(self, branches, value = 0):
		for branch in branches:
			assert isinstance(branch, MiniMaxTree), "Branch is not a MiniMaxTree"


	def static_evaluation(self, state):
		return None


a = [[[0, 0], [0, 0]],[[0,0],[0,0]]]

