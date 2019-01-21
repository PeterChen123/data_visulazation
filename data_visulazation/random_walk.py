from random import choice

class RandomWalk():
	#create a class for generating random data
	
	def __init__(self, num_points = 5000):
		#reset all variables
		self.num_points = num_points
		
		#let all the walks started from (0,0)
		self.x_values = [0]
		self.y_values = [0]
	
	def fill_walk(self):
		#calculate all the points in the walk
		
		while len(self.x_values) < self.num_points:
			x_direction = choice([-1,1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction * x_distance

			y_direction = choice([-1,1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance
			
			#do not stay at the same point
			if x_step == 0 and y_step == 0:
				continue
				
			#calculate the value of next point
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)