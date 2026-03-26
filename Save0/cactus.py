from std import *

def plant_cactus(type):
	def f():
		plant(type)
	return f

def sort(dir1,dir2):
	def bubble():
		while True:
			flg = 1
			for i in range(get_world_size()):
				if i != get_world_size()-1 and measure() > measure(dir1):
					flg = 0
					swap(dir1)
				move(dir1)
			if flg:
				break
	go(0,0)
	for i in range(get_world_size()):
		if not spawn_drone(bubble):
			bubble()
		move(dir2)
	while num_drones() > 1:
		pass

def get_cactus(num):
	init()
	start = num_items(Items.Cactus)
	while num_items(Items.Cactus)-start < num:
		for_all(plant_cactus(Entities.Cactus))
		sort(North,East)
		sort(East,North)
		harvest()
