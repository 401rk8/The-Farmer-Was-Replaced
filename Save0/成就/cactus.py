from std_farm import *

def sort(dir1,dir2):
	def bubble():
		while True:
			flg = 1
			for i in range(n):
				if i != n-1 and measure() > measure(dir1):
					flg = 0
					swap(dir1)
				move(dir1)
			if flg:
				break
	for i in range(n):
		if not spawn_drone(bubble):
			bubble()
		move(dir2)
	while num_drones() > 1:
		pass
	go(0,0)

while True:
	for_all(plant1(Entities.Cactus))
	sort(North,East)
	sort(East,North)
	harvest()
