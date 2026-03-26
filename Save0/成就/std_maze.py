from std import *

dir = (North,East,South,West)
dlt = {North:(0,1), East:(1,0), South:(0,-1), West:(-1,0)}

m = 5
substance = m * 2**(num_unlocked(Unlocks.Mazes) - 1)

def gen():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)

dlt_maze = []
for i in range(m):
	if i%2 == 0:
		for j in range(m):
			dlt_maze.append((i,j))
	else:
		for j in range(m-1,-1,-1):
			dlt_maze.append((i,j))
dlt_maze.pop(0)
