import math
import numpy as np 
class vector2:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.angle = math.degrees(math.atan(self.x, self.y))
		self.numpy = np.array([self.x, self.y])
	
	def Foreward(self, distance):
		x2 = self.x + Math.cos(0) * distance
		y2 = self.y + Math.sin(0) * distance
		self.x = self.x + Math.cos(0) * distance
		self.y = self.y + Math.sin(0) * distance
		return [(self.x, self.y),(x2, y2)]

	def turnClockWise(self, angle):
		rotMatrix = np.array([[math.cos(-angle), -math.sin(-angle)], [math.sin(-angle), math.cos(-angle)]])
		curVec = np.array([[self.x], [self.y]])
		returnVec = np.matmul(rotMatrix * curVec)
		self.x = returnVec.item(0)
		self.y = returnVec.item(1)

	def turnAntiWise(self, angle):
		rotMatrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
		curVec = np.array([[self.x], [self.y]])
		returnVec = np.matmul(rotMatrix * curVec)
		self.x = returnVec.item(0)
		self.y = returnVec.item(1)