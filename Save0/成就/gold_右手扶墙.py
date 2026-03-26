from std_maze import *

i = 0
while True:
	gen()
	while get_entity_type() != Entities.Treasure:
		if can_move(dir[i]):
			move(dir[i])
			if can_move(dir[(i+1)%4]):
				i = (i + 1) % 4
		else:
			i = (i + 3) % 4
	harvest()
