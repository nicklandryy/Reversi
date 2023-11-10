import pygame
import random
import copy

class Reversi:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1100, 800))
		pygame.display.set_caption("Reversi")

		self.runGame = True

	def run(self):
		while(self.runGame == True):
			self.input()
			self.update()
			self.draw()


	def input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.runGame = False


	def update(self):
		pass


	def draw(self):
		self.screen.fill((0, 0, 0))

		pygame.display.update()

	class Grid:
		def __init__(self, rows, columns, size, main) -> None:
			self.GAME = main
			self.i = rows
			self.j = columns
			self.size = size

			self.gridLogic = self.regenerateGrid(self.i, self.j)
		
		def regenerateGrid(self, rows, columns):
			
	
if __name__ == '__main__':
	game = Reversi()
	game.run()
	pygame.quit()