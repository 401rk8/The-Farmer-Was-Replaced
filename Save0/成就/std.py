n = get_world_size()
set_world_size(n)
#set_execution_speed(4)
clear()

def get_pos():
	return (get_pos_x(), get_pos_y())

def go(x,y):
	if (x-get_pos_x()+n) % n < n//2:
		dir = East
	else:
		dir = West
	while get_pos_x() != x:
		move(dir)
	if (y-get_pos_y()+n) % n < n//2:
		dir = North
	else:
		dir = South
	while get_pos_y() != y:
		move(dir)

def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

def wait_all():
	while num_drones() > 1:
		pass
