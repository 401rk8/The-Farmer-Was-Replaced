from std_farm import *

def plant_wood():
	if (get_pos_x() + get_pos_y()) % 2:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
	water()

for_all(plant_wood)
wait_all()
go(0,0)

def main(sx,sy):
	def f():
		change_hat(Hats.Top_Hat)
		go(sx,sy)
		do_a_flip()
		
		while True:
			for i in range(n):
				water()
				if get_entity_type() == Entities.Tree and can_harvest():
					type,(x,y) = get_companion()
					wait_for(spawn_drone(go_plant(x,y,type)))
					harvest()
					if (x + y) % 2:
						wait_for(spawn_drone(go_plant(x,y,Entities.Tree)))
					plant(Entities.Tree)
				
				move(North)
			move(East)
	return f

for i in range(3,-1,-1):
	for j in range(3,-1,-1):
		spawn_drone(main(i*8+7-j*2,j*8))
