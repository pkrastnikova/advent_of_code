f = open('day3_part1_ex.txt', "r")
lines = f.readlines()
matrix = []
result = 0

for line in lines:
    row_list = []
    for i in range(len(line)):
        row_list.append(line[i].strip())
    matrix.append(row_list)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
     
# find adjacents of a seat
# i - line (row), j - seat in the line (column)

M = len(matrix)  # number of rows (lines)
N = len(matrix[0]) # number of columns


def get_adj(i, j):

    # upper left
    if i == 0 and j == 0:
        adj_seats = [0, 1, 'right'], [1, 0, 'down'], [1, 1, 'diag_down_right']  
    # upper right
    elif i == 0 and j == N - 1:
        adj_seats = [0, N-2, 'left'], [1, N-2, 'diag_down_left'], [1, N-1, 'down']
    # bottom left
    elif i == M-1 and j == 0:
        adj_seats = [M-2, 0, 'up'], [M-2, 1, 'diag_up_right'], [M-1, 1, 'right']
    # bottom right
    elif i == M-1 and j == N-1:
        adj_seats = [M-1, N-2, 'left'], [M-2, N-2, 'diag_up_left'], [M-2, N-1, 'up']
    # first column
    elif j == 0:
        adj_seats = [i-1, 0, 'up'], [i-1, 1, 'diag_up_right'], [i, 1, 'right'], [i+1, 1, 'diag_down_right'], [i+1, 0, 'down']
    # last column
    elif j == N-1:
        adj_seats = [i-1, N-1, 'up'], [i-1, N-2, 'diag_up_left'], [i, N-2, 'left' ], [i+1, N-2, 'diag_down_left'], [i+1, N-1, 'down']
    # first row
    elif i == 0:
        adj_seats = [0, j-1, 'left'], [0, j+1, 'right'], [1, j, 'down'], [1, j-1, 'diag_down_left'], [1, j+1, 'diag_down_right']
    # last row:
    elif i == M-1:
        adj_seats = [M-1, j-1, 'left'], [M-1, j+1, 'right'], [M-2, j, 'up'], [M-2, j-1, 'diag_up_left'], [M-2, j+1, 'diag_up_right']
    else:
        adj_seats = [i, j-1, 'left'], [i, j+1, 'right'], [i-1, j, 'up'], [i-1, j+1, 'diag_up_right'], [i-1, j-1, 'diag_up_left'], \
             [i+1, j, 'down'], [i+1, j-1, 'diag_down_left'], [i+1, j+1, 'diag_down_right']
    
    return adj_seats

def get_adj2(i, j_first, j_last): #call with first and last j index of the number found

    adj_pairs = list()
    if j_first > 0:
        adj_pairs.append((i, max(0, j_first-1)))
    
    if j_last < N-1:
        adj_pairs.append((i, min(N, j_last+1)))
    
    for j in range(j_first-1, j_last+2):
        if i != 0 and j_first > 0 and j_last < M:
            adj_pairs.append((i-1, j))
        if i != M and j_last < N-1 and j_first > 0:
            adj_pairs.append((i+1, j))
    
    return adj_pairs

    


print(get_adj(0, 0))
print(get_adj(0, 1))
print(get_adj(0, 2))
print(get_adj(1, 3))

def check_adj(adj_list):    
    for adj in adj_list:
        i = adj[0]
        j = adj[1]
        if matrix[i][j] != ".":
            print("matrix[i][j]: ", matrix[i][j])
            return True
    return False



def engine_schematic(m):
    result = 0
    for i in range(len(m)):
        number = ''
        indeces = list()
        j = 0
        while j < len(m[i]):
            if m[i][j].isnumeric():
                number += m[i][j]
                indeces.append(j)
            else:
               print("indeces: ", indeces)
               if len(indeces) > 0: #found a number
                   adj = get_adj2(i, indeces[0], indeces[-1])
                   print(adj)
                  

                   '''              
                   if check_adj(adj):
                        result += int(number, base=10)
                        print("Found number: ", number)
                        number = ''
                        indeces = list()
                        break
                    '''
                       
            j+=1
    
    print(result)

engine_schematic(matrix)





 
