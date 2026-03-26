from std_farm import *

def main(sx,sy):
	def f():
		change_hat(Hats.Top_Hat)
		go(sx,sy)
		till()
		do_a_flip()
		
		while True:
			water()
			type,(x,y) = get_companion()
			wait_for(spawn_drone(go_plant(x,y,type)))
#			if not can_harvest():
#				print("WA")
			harvest()
	return f

for i in range(3,-1,-1):
	for j in range(3,-1,-1):
		spawn_drone(main(i*7+3,j*7+3))
