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

item_to_entity = {Items.Hay:Entities.Grass,
				  Items.Wood:Entities.Bush,
				  Items.Carrot:Entities.Carrot,
				  Items.Pumpkin:Entities.Pumpkin,
				  Items.Cactus:Entities.Cactus,
				  Items.Power:Entities.Sunflower}

n = 0

def init(x=-1):
	global n
	if x == -1:
		n = get_world_size()
	else:
		n = x
	clear()
	set_world_size(n)
	for_all(till)

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
