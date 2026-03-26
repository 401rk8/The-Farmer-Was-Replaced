for i in Unlocks:
	for j in range(num_unlocked(i)):
		quick_print(i, get_cost(i,j))
	quick_print("")
