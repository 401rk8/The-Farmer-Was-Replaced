# n = 8, m = 4

from std_maze import *

def work():
	while True:
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, substance)

def main(x,y,op):
	def f():
		go(x,y)
		for i,j in dlt_maze:
			go(x+op*i,y+op*j)
			spawn_drone(work)
		go(x,y)
	
		t = get_time()
		gen()

		while True:
			if get_entity_type() == Entities.Treasure:
				use_item(Items.Weird_Substance, substance)
			if get_time()-t > 8:
				harvest()
				harvest()
				t = get_time()
				gen()
	return f

spawn_drone(main(n-1,n-1,-1))
main(0,0,1)()
