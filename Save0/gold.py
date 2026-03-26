from std import *

def main(x,y):
	m = 5
	substance = m * 2**(num_unlocked(Unlocks.Mazes) - 1)
	dir = (North,East,South,West)
	dlt = {North:(0,1), East:(1,0), South:(0,-1), West:(-1,0)}
	dlt_maze = []
	for i in range(m):
		if i%2 == 0:
			for j in range(m):
				dlt_maze.append((i,j))
		else:
			for j in range(m-1,-1,-1):
				dlt_maze.append((i,j))
	dlt_maze.pop(0)

	def f():
		go(x,y)
		do_a_flip()
		
		vis = set()
		def dfs(t):
			u = (get_pos_x(),get_pos_y())
			if u == t:
				return True
			vis.add(u)
			for i in range(4):
				if can_move(dir[i]):
					v = dlt[dir[i]]
					if (u[0]+dlt[dir[i]][0],u[1]+dlt[dir[i]][1]) in vis:
						continue
					move(dir[i])
					if dfs(t):
						return True
					move(dir[(i+2)%4])
			return False
		
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, substance)
		vis = set()
		dfs(measure())
		harvest()
		go(0,0)
	return f

def get_gold(num):
	init()
	while num_items(Items.Gold) < num:
		for i in range(get_world_size()-5,-1,-5):
			flg = False
			for j in range(get_world_size()-5,-1,-5):
				if not spawn_drone(main(i+2,j+2)):
					main(i+2,j+2)()
					flg = True
					break
			if flg:
				break
		while num_drones() > 1:
			pass
