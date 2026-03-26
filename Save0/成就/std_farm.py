from std import *

for_all(till)
wait_all()
go(0,0)

def water():
	while get_water() < 0.75:
		use_item(Items.Water)

def plant1(entity):
	def f():
		plant(entity)
		water()
	return f

def go_plant(x,y,type):
	def f():
		go(x,y)
		harvest()
		plant(type)
	return f

def Entities_Wood():
	if (get_pos_x()+get_pos_y())%2 == 0:
		return Entities.Tree
	else:
		return Entities.Bush
def Entities_Hay_Wood_Carrot():
	if get_pos_x()%2 == 0:
		if get_pos_y()%2 == 0:
			return Entities.Grass
		else:
			return Entities.Bush
	else:
		if get_pos_y()%2 == 0:
			return Entities.Tree
		else:
			return Entities.Carrot

dlt_pumpkin = []
for i in range(6):
	if i%2 == 0:
		for j in range(6):
			dlt_pumpkin.append((i,j))
	else:
		for j in range(5,-1,-1):
			dlt_pumpkin.append((i,j))
