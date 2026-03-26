from std import *

dlt_pumpkin = []
for i in range(6):
	if i%2 == 0:
		for j in range(6):
			dlt_pumpkin.append((i,j))
	else:
		for j in range(5,-1,-1):
			dlt_pumpkin.append((i,j))

def chk(x,y,tot):
	def f():
		pos1 = dlt_pumpkin
		while True:
			flg = 1
			pos2 = []
			for i,j in pos1:
				go(x+i,y+j)
				if not can_harvest():
					flg = 0
					pos2.append((i,j))
					if get_entity_type() != Entities.Pumpkin:
						plant(Entities.Pumpkin)
			if flg == 1:
				harvest()
				if num_items(Items.Pumpkin) >= tot:
					return
				pos1 = dlt_pumpkin
			else:
				pos1 = pos2
	return f

def get_pumpkin(num):
	init()
	tot = num_items(Items.Pumpkin) + num
	for x in range(0,get_world_size(),7):
		for y in range(0,get_world_size(),7):
			if x+6 <= get_world_size() and y+6 <= get_world_size():
				if not spawn_drone(chk(x,y,tot)):
					chk(x,y,tot)()
