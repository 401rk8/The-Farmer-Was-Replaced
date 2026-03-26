from std_farm import *

def plant_pumpkin():
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)

while True:
	for_all(plant_pumpkin)
