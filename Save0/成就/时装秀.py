set_world_size(5)
clear()

def f(hat):
	def g():
		change_hat(hat)
		for i in range(9):
			do_a_flip()
	return g

spawn_drone(f(Hats.Straw_Hat))
move(North)
spawn_drone(f(Hats.Carrot_Hat))
move(North)
spawn_drone(f(Hats.Pumpkin_Hat))
move(North)
spawn_drone(f(Hats.Cactus_Hat))
move(North)
spawn_drone(f(Hats.Sunflower_Hat))
move(North)
