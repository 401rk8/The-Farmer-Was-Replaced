from std import *
from pumpkin import get_pumpkin
from cactus import get_cactus
from gold import get_gold
from bone import get_bone

def get_wood(num):
	def plant_and_harvest():
		if can_harvest():
			harvest()
		if get_entity_type() == None:
			if get_pos_x()%2 == get_pos_y()%2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
	start = num_items(Items.Wood)
	while num_items(Items.Wood)-start < num:
		for_all(plant_and_harvest)

def get_weird(num):
	def plant_and_harvest():
		if can_harvest():
			harvest()
		if get_entity_type() == None:
			plant(Entities.Grass)
			use_item(Items.Fertilizer)
	while num_items(Items.Weird_Substance) < num:
		for_all(plant_and_harvest)

def get(item, num):
	if item == Items.Weird_Substance:
		get_weird(num)
		return
	if item == Items.Gold:
		get_weird(num//5)
		get_gold(num)
		return
	if item == Items.Bone:
		get_bone(num)
		return
	
	type = item_to_entity[item]
	for i in get_cost(type):
		get(i, num)
	
	if item == Items.Wood and num_unlocked(Unlocks.Trees):
		get_wood(num)
		return
	if item == Items.Pumpkin:
		get_pumpkin(num)
		return
	if item == Items.Cactus:
		get_cactus(num)
		return
	
	def plant_and_harvest():
		if can_harvest():
			harvest()
		if get_entity_type() == None:
			plant(type)
	start = num_items(item)
	while num_items(item)-start < num:
		for_all(plant_and_harvest)

def get_dict(cost):
	init()
	for i in cost:
		get(i, cost[i])
