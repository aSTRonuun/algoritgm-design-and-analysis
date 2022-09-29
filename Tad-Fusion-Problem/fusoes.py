from ctypes import Union
from uniofind import UnionFind	

def fusoes(uf, command, x, y):
	# O(1)
	if command == 'F':
		uf.union(x, y)
	# O(1)	
	elif command == 'C':
		if uf.connected(x, y):
			print('S') 
		else:
			print('N')


# main
if __name__ == "__main__":
    
	qtd_banks, qtd_fusoes = map(int, input().split())
	# O(n)
	uf = UnionFind(range(1, qtd_banks + 1))

	print(uf)

	# O(n)
	for i in range(qtd_fusoes):
		command, bank1, bank2 = input().split()

		
		fusoes(uf, command, int(bank1), int(bank2))
		

	
            



        



