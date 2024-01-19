from typing import Tuple, List

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	block_num = 0
	# for i in range (8):
	# 	for j in range (8):
	if pos[0] <= 3 and pos[1] <= 3:
		block_num = 1
	elif pos[0] <= 3 and 3<pos[1] <= 6:
		block_num = 2
	elif pos[0] <= 3 and 6<pos[1] <= 9:
		block_num = 3
	elif 3<pos[0] <= 6 and pos[1] <= 3:
		block_num = 4
	elif 3<pos[0] <= 6 and 3<pos[1] <= 6:
		block_num = 5
	elif 3<pos[0] <= 6 and 6<pos[1] <= 9:
		block_num = 6
	elif 6<pos[0] <= 9 and pos[1] <= 3:
		block_num = 7
	elif 6<pos[0] <= 9 and 3<pos[1] <= 6:
		block_num = 8
	elif 6<pos[0] <= 9 and 6<pos[1] <= 9:
		block_num = 9
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""

	return block_num

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	
	x = get_block_num(sudoku, pos)
	for k in range(0,3):
		if 3*k < x <=3*(k+1):
			m = k
	if pos[0] == 3*m+1 :
		if 1<= pos[1] <= 3:
			index = pos[1]
		if 4<= pos[1] <= 6:
			index = pos[1] - 3
		if 7<=pos[1] <= 9:
			index = pos[1] - 6

	elif pos[0] == 3*m+2 :
		if 1<= pos[1] <= 3:
			index = pos[1] + 3
		if 4<= pos[1] <= 6:
			index = pos[1] 
		if 7<=pos[1] <= 9:
			index = pos[1] - 3

	elif pos[0] == 3*m+3:
		if 1<= pos[1] <= 3:
			index = pos[1] + 6
		if 4<= pos[1] <= 6:
			index = pos[1] + 3
		if 7<=pos[1] <= 9:
			index = pos[1] 


	return index


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	if x == 1:
		block = (sudoku[0][0:3]+sudoku[1][0:3]+sudoku[2][0:3])
	if x == 2:
		block = (sudoku[0][3:6]+sudoku[1][3:6]+sudoku[2][3:6])
	if x == 3:
		block = (sudoku[0][6:9]+sudoku[1][6:9]+sudoku[2][6:9])
	if x == 4:
		block = (sudoku[3][0:3]+sudoku[4][0:3]+sudoku[5][0:3])
	if x == 5:
		block = (sudoku[3][3:6]+sudoku[4][3:6]+sudoku[5][3:6])
	if x == 6:
		block = (sudoku[3][6:9]+sudoku[4][6:9]+sudoku[5][6:9])
	if x == 7:
		block = (sudoku[6][0:3]+sudoku[7][0:3]+sudoku[8][0:3])
	if x == 8:
		block = (sudoku[6][3:6]+sudoku[7][3:6]+sudoku[8][3:6])
	if x == 9:
		block = (sudoku[6][6:9]+sudoku[7][6:9]+sudoku[8][6:9])
	
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""

	return block
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	row_list = sudoku[i-1]
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""

	return row_list

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	column = []
	for i in range (len(sudoku)):
		column.append(sudoku[i][x-1])

	return column

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	row = -1
	column = -1
	for i in range (9):
		for j in range (9):
			if sudoku[8-i][8-j] == 0:
				row = 9-i 
				column = 9-j
	


	return (row,column)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	x = True
	for i in range(1,10):
		a = lst.count(i)
		if a > 1:
			x = False
			break
	return x


	

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	x = True
	for i in range (9):
		x = valid_list(sudoku[i])
		if x == False:
			break 
		else:
			for j in range (1,10):
				x = valid_list(get_column(sudoku,j))
				if x == False:
					break
				else:
					for k in range (1,10):
						x = valid_list(get_block(sudoku,k))
						if x == False:
							break


	return x


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	row_list = []
	column_list = []
	block_list = []
	
	intersection_1 = []
	intersection_2 = []

	row_index = pos[0] 
	column_index = pos[1] 
	block_num = get_block_num(sudoku,pos)

	for i in range (1,10):
		sudoku[row_index-1][column_index-1] = i
		x =  valid_list(get_row(sudoku,row_index))
		if x == True:
			row_list.append(i)

		
		y =  valid_list(get_column(sudoku,column_index))
		if y == True:
			column_list.append(i)

		
		z = valid_list(get_block(sudoku,block_num))
		if z == True:
			block_list.append(i)
	
	if len(row_list)>len(column_list):
		row_list , column_list = column_list , row_list

	
	for i in range (len(row_list)):
		if row_list[i] in column_list:
			intersection_1.append(row_list[i])
	
	if len(intersection_1) > len(block_list):
		intersection_1 , block_list = block_list , intersection_1

	
	for i in range (len(intersection_1)):
		if intersection_1[i] in block_list:
			intersection_2.append(intersection_1[i])


	return intersection_2

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1] = num

	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1] = 0

	return sudoku


def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	
	unassigned_position_list = []
	for i in range (0,9):
		for j in range (0,9):
			if sudoku[i][j] == 0:
				unassigned_position_list.append((i+1,j+1))
	
	sudoku_copy = sudoku.copy()
	unassigned_position_list_1 = []
	for i in range (0,9):
		for j in range (0,9):
			if sudoku_copy[i][j] == 0:
				unassigned_position_list_1.append(1)
	
	
	if len(unassigned_position_list_1) == 0:
		return (True,sudoku_copy)
		
	else:
		first_unassigned_position = find_first_unassigned_position(sudoku_copy)
		possible_candidates = get_candidates(sudoku_copy,first_unassigned_position)
		
		z =first_unassigned_position
		
		
		
		if len(possible_candidates) != 0:
			for i in range (len(possible_candidates)):
				
				sudoku_copy = make_move(sudoku_copy,first_unassigned_position,possible_candidates[i])
				
				
				if sudoku_solver(sudoku_copy)[0]:
					return (True,sudoku_solver(sudoku_copy)[1])
		
				
		elif len(possible_candidates) == 0:
				for k in range (len(unassigned_position_list)):
					if unassigned_position_list[k][0] < first_unassigned_position[0]:
						z = unassigned_position_list[k][0],  unassigned_position_list[k][1]
					elif unassigned_position_list[k][0] == first_unassigned_position[0]:
						if unassigned_position_list[k][1] < first_unassigned_position[1]:
							z = unassigned_position_list[k][0],  unassigned_position_list[k][1]
				
				sudoku_copy = undo_move(sudoku_copy,first_unassigned_position)
				sudoku_copy = undo_move(sudoku_copy,z)
				
				
	sudoku_copy = undo_move(sudoku,first_unassigned_position)		
	return (False,sudoku_copy)

# 	print("Testcases for In Lab evaluation")
# 	print("Get Block Number:")
# 	print(get_block_num(sudoku,(4,4)))
# 	print(get_block_num(sudoku,(7,2)))
# 	print(get_block_num(sudoku,(2,6)))
# 	print("Get Block:")
# 	print(get_block(sudoku,3))
# 	print(get_block(sudoku,5))
# 	print(get_block(sudoku,9))
# 	print("Get Row:")
# 	print(get_row(sudoku,3))
# 	print(get_row(sudoku,5))
# 	print(get_row(sudoku,9))

# Following is the driver code

if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	
	possible, sudoku = sudoku_solver(sudoku)

	# Check if it could be solved
	
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)

