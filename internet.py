import random
from helper import *

class Internet:
	def __init__(self):
		# if(n % 2 == 0):
		# 	n += 1
		self.grid = [[None for x in range(1001)] for y in range(1001)]
		self.ip_data = {}
		self.n = 1001

	def __scanring(self, x, y, i):
		x1 = (x - i) % self.n
		x2 = (x + i) % self.n
		y1 = (y - i) % self.n
		y2 = (y + i) % self.n

		for j in range(2*i + 1):
			curr_x = (x1 + j)%self.n
			curr_y = y1

			# print(curr_x, curr_y)

			if (curr_x, curr_y) in self.ip_data:
				return self.ip_data[(curr_x, curr_y)]

		for j in range(1, 2*i + 1):
			curr_x = x2
			curr_y = (y1 + j)%self.n

			# print(curr_x, curr_y)

			if (curr_x, curr_y) in self.ip_data:
				return self.ip_data[(curr_x, curr_y)]

		for j in range(1, 2*i + 1):
			curr_x = (x2 - j)%self.n
			curr_y = y2

			# print(curr_x, curr_y)

			if (curr_x, curr_y) in self.ip_data:
				return self.ip_data[(curr_x, curr_y)]

		for j in range(1, 2*i):
			curr_x = x1
			curr_y = (y2 - j)%self.n

			# print(curr_x, curr_y)

			if (curr_x, curr_y) in self.ip_data:
				return self.ip_data[(curr_x, curr_y)]
		return None


	def getNearestNode(self, x, y):
		# print("Scanning with {} {}".format(x, y))
		for i in range(self.n//2):
			curr = self.__scanring(x, y, i+1)
			if(curr != None):
				return curr 

		return None

	def getIp(self, node):
		while(True):
			curr = random.randint(0, self.n**2-1)
			x = curr//self.n
			y = curr%self.n
			if (x, y) not in self.ip_data:
				break
		# print(x, y)
		self.ip_data[(x, y)] = node
		return x, y

