from std_farm import *

def chk(x,y):
	def f():
		change_hat(Hats.Pumpkin_Hat)
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
				pos1 = dlt_pumpkin
			else:
				pos1 = pos2
	return f

for x in range(0,n,7):
	for y in range(0,n,7):
		if x+6 <= n and y+6 <= n:
			spawn_drone(chk(x,y))

def main():
	water()
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return
	if get_pos_x() > 27 or get_pos_y() > 27:
		if can_harvest():
			harvest()
		if get_entity_type() == None:
			plant(Entities.Pumpkin)

while True:
	for_all(main)
