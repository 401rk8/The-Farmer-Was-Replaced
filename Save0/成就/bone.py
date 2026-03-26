n = get_world_size()
set_world_size(n)
#set_execution_speed(4)
clear()

def go(x,y):
	while get_pos_y() < y:
		if not move(North):
			break
	while get_pos_y() > y:
		if not move(South):
			break
	while get_pos_x() < x:
		if not move(East):
			break
	while get_pos_x() > x:
		if not move(West):
			break
	while get_pos_y() < y:
		if not move(North):
			return False
	while get_pos_y() > y:
		if not move(South):
			return False
	while get_pos_x() < x:
		if not move(East):
			return False
	while get_pos_x() > x:
		if not move(West):
			return False
	return True

while True:
	change_hat(Hats.Dinosaur_Hat)
	flg = True
	for i in range(n):
		x,y = measure()
		if not go(x,y):
			flg = False
			break
	if not flg:
		change_hat(Hats.Green_Hat)
		continue
	go(0,0)
	while True:
		for j in range(n-1):
			move(North)
		if not move(East):
			change_hat(Hats.Green_Hat)
			break
		for j in range(n):
			for i in range(n-2):
				if get_pos_y() % 2 == 1:
					move(East)
				else:
					move(West)
			if get_pos_y() != 0:
				move(South)
			else:
				move(West)
