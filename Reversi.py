import pygame
import random
import copy

class Reversi:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1100, 800))