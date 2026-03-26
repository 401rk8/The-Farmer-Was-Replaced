from std_farm import *

for_all(plant1(Entities.Carrot))
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
				if get_entity_type() == Entities.Carrot:
					type,(x,y) = get_companion()
					wait_for(spawn_drone(go_plant(x,y,type)))
					while not can_harvest():
						pass
				harvest()
				plant(Entities.Carrot)
				
				move(North)
			move(East)
	return f

for i in range(3,-1,-1):
	for j in range(3,-1,-1):
		spawn_drone(main(i*8+7-j*2,j*8))
