import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self,numpoints=5000):
        """Initialize attributes of a walk"""
        self.num_points = numpoints
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all points in the walk"""
        while len(self.x_values) < self.num_points:
            # decide which direction to go and how far to go
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance

            x = (self.x_values[-1]+x_step)
            y = (self.y_values[-1]+y_step)
            self.x_values.append(x)
            self.y_values.append(y)

rw = RandomWalk()
rw.fill_walk()
rw.point_numbers = range(rw.num_points)
plt.style.use('classic')
fig, ax = plt.subplots()
plt.title("Random Walk Pattern")
plt.xkcd()
ax.scatter(rw.x_values,rw.y_values,s=15,c=rw.point_numbers,cmap=plt.cm.plasma,edgecolors='none')
ax.scatter(0,0,s=100,color='green',edgecolors='none')
ax.scatter(rw.x_values[-1],rw.y_values[-1],s=100,color='red',edgecolors='none')

ax.set_aspect('equal')

plt.show()