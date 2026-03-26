# The-Farmer-Was-Replaced

## Tricks

默认 `set_world_size(n)`，水分和能量充足

- 移动到给定位置：

```python 
def go(x,y):
	if (x-get_pos_x()+n) % n < n/2:
		dir = East
	else:
		dir = West
	while get_pos_x() != x:
		move(dir)
	if (y-get_pos_y()+n) % n < n/2:
		dir = North
	else:
		dir = South
	while get_pos_y() != y:
		move(dir)
```

- 并行种植：

```python
def plant1(entity):
	def f():
		plant(entity)
	return f

for_all(plant1(Entities.))
```

- 等待所有并行结束：

```python
while num_drones() > 1:
	pass
```

## Items

### Wood

```python
def Entities_Wood():
	if (get_pos_x() + get_pos_y()) % 2:
		return Entities.Tree
	else:
		return Entities.Bush
```

### Cactus

容易证明先对每一行冒泡排序、再对每一列冒泡排序是合法的

### Bone

手玩一个 Hamilton 回路即可，比如 $n$ 为偶数时

```plain
^>>v
^v<<
^>>v
^<<<
```

$n$ 较大时可以前 $n$ 次径直前往下一个苹果（大概率不会撞到尾巴）

### Gold

生成迷宫会尽量以无人机所在位置为中心

右手扶墙和 dfs 都值得一写

## 竞速成就

信息窗口中的「统计数据」可以看到过去 60s 的收获

> 恐龙大师：1 分钟内收获 1M 骨头

填满 $14\times14$ 的农场刚好够，但我最快也要 90s

实际上只要求平均 1M/min，完成「长度很重要」时可以顺便完成

「仙人掌大师」同理

> 迷宫大师：1 分钟内收获 2M 黄金

第一想法是并行 bfs，然而并不会写

发现单无人机 dfs $5\times5$ 的迷宫就有 0.07M/min ^_^

据说填满两个 $4\times4$ 迷宫最优（过于神秘。如何想到），但我只能做到 1.8M/min

> 南瓜大师：1 分钟内收获 20M 南瓜

每个无人机负责一个 $6\times6$ 南瓜（维护 `Dead_Pumpkin` 的位置列表），剩下的遍历农场，发现 `Dead_Pumpkin` 就重种即可

> 干草大师：1 分钟内收获 2B 干草

需要利用「混合种植」。基本思路是主无人机在 $7\times7$ 正方形中心种草，`wait_for(spawn_drone(` 种伴生植物

由于草长得过于之快，`wait_for` 后直接 `harvest` 即可

> 胡萝卜大师：1 分钟内收获 2B 胡萝卜

胡萝卜长得不够快，等待 `can_harvest()` 即可

> 木材大师：1 分钟内收获 10B 木材

个人认为最困难的一个

树长得更慢所以不能原地等待，需要移动起来，然而伴生植物的随机性会导致主无人机逐渐靠近后互相影响

我的做法是大力尝试排列组合优化常数（详见代码），最终也只是勉强通过

另一个想法是强制令分身 `move` $3$ 次，这样主无人机应该会跟最慢的保持一致，不知道可不可行

## 「全自动化」

建议先仔细阅读三种 `import` 的区别，跨文件多使用函数而非变量

我的目标是尽量简单地完成

1. 打印所有花费并手玩一个解锁序列出来，按解锁新物品分块。最好方便后面调整顺序
2. 逐个实现 `get(item, num)`（不考虑水分、能量、混合种植），种植有花费的递归下去即可（花费和产量始终是 $1:1$ 的）

我 `Dinosaur, Maze` 都解锁了 $4$ 级，绝对过剩了。另外由于 `world_size, max_drones` 不够似乎「迷宫大师」的做法并不优
