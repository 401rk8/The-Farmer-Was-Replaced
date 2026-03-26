from std_maze import *

def main(x,y):
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
		while True:
			plant(Entities.Bush)
			for i in range(300):
				use_item(Items.Weird_Substance, substance)
				vis = set()
				dfs(measure())
			harvest()
			go(x,y)
	return f

for i in range(n-5,-1,-5):
	for j in range(n-5,-1,-5):
		if not spawn_drone(main(i+2,j+2)):
			main(i+2,j+2)()
