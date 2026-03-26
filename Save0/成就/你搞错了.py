n = 4
set_world_size(n)
for i in range(n):
	for j in range(n):
		till()
		plant(Entities.Cactus)
		move(North)
	move(East)
while True:
	for i in range(n):
		for j in range(n):
			if j < n and measure() < measure(North):
				swap(North)
			if i < n and measure() < measure(East):
				swap(East)
			move(North)
		move(East)