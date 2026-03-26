from std_maze import *

T = get_time()

vis = set()
def dfs(t):
	global vis
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
for i in range(300):
	use_item(Items.Weird_Substance, substance)
	vis = set()
	dfs(measure())

print(get_time()-T)
