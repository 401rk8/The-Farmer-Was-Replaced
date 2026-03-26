from std_farm import *

for_all(plant1(Entities.Sunflower))

def main():
	if can_harvest():
		harvest()
		plant(Entities.Sunflower)
		water()

while True:
	for_all(main)
