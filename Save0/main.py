from std import *

def unlock_(lock):
	unlock(lock)
	quick_print(lock, num_unlocked(lock))

def unlock_list(lis):
	from farm import get_dict
	for lock in lis:
		get_dict(get_cost(lock))
		unlock_(lock)
	quick_print("\n################################\n")


for lock in [Unlocks.Speed, Unlocks.Expand, Unlocks.Plant]:
	while num_items(Items.Hay) < get_cost(lock)[Items.Hay]:
		if can_harvest():
			harvest()
		move(North)
	unlock_(lock)

quick_print("\n################################\n")


unlock_list([Unlocks.Speed, Unlocks.Expand, Unlocks.Carrots])

unlock_list([Unlocks.Expand,
Unlocks.Speed,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Expand,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Carrots,
Unlocks.Pumpkins,
Unlocks.Sunflowers,
Unlocks.Fertilizer])

unlock_list([Unlocks.Speed,
Unlocks.Expand,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Carrots,
Unlocks.Pumpkins,
Unlocks.Fertilizer,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Carrots,
Unlocks.Pumpkins,
Unlocks.Cactus])

unlock_list([Unlocks.Speed,
Unlocks.Expand,
Unlocks.Grass,
Unlocks.Trees,
Unlocks.Carrots,
Unlocks.Pumpkins,
Unlocks.Cactus,
Unlocks.Fertilizer,
Unlocks.Dinosaurs,
Unlocks.Fertilizer,
Unlocks.Dinosaurs,
Unlocks.Mazes])

unlock_list([Unlocks.Expand,
Unlocks.Mazes,
Unlocks.Megafarm,
Unlocks.Dinosaurs,
Unlocks.Mazes,
Unlocks.Megafarm,
Unlocks.Dinosaurs,
Unlocks.Mazes,
Unlocks.Megafarm])

from farm import get
get(Items.Bone, 2000000)
get(Items.Gold, 1000000)
unlock_(Unlocks.Leaderboard)

# for i in Unlocks:
# 	if num_unlocked(i) > 0:
# 		quick_print(i,num_unlocked(i))
# while True:
# 	pass
