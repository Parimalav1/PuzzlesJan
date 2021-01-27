Consider a matrix where each cell contains either a 0 or a 1 and any cell containing a 1 is called a filled cell. Two cells are said to be connected 
if they are adjacent to each other horizontally, vertically, or diagonally.In the diagram below, the two colored regions show cells connected to the filled cells. 
Black are not connected.
Cells adjacent to filled cells: 🔴🔴🔴⚫️🔵 1
                                🔴1 🔴⚫️🔵🔵
                                🔴🔴🔴⚫️⚫️⚫️ 

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region 
but is not necessarily directly connected to all the other cells in the region.
Regions: 110001
         011000
         000100

Given an n*m matrix, find and print the number of cells in the largest region in the matrix.

Function Description:
Complete the function maxRegion in the editor below. It must return an integer value, the size of the largest region.

maxRegion has the following parameter(s):
grid: a two dimensional array of integers
Input Format
The first line contains an integer, , the number of rows in the matrix, grid.
The second line contains an integer, , the number of columns in the matrix.
Each of the following  lines contains a row of  space-separated integers, grid[i][j].

Constraints: 0 < n,m < 10

Sample Input:   -> Output: 5
4 * 4               
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

# define rows and columns, iterate thru them
# define a set, if the cell value equals 1, append it to set
# check if cell has adjacent or below, then append it to set
# keep a track of max cells, either recursive or iterative
# find the max no of cells and return it

visited = set()
def maxRegionRecursive(grid, i, j):
    while i>0 or j>0 and i<= len(grid) or j <= len(grid[0]):
        if grid[i][j] == 0:
            return 0
        if (i,j) in visited:
            return 0
        count = 1
        visited.add((i,j))
        count += maxRegionRecursive(grid, i, j+1)

def maxRegion(grid):
    maxSize = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxSize = max(maxSize, maxRegionRecursive(grid, i, j))

    return maxSize

    # iteratively adding to count from the previous line ie. 49
  count += maxRegionRecursive(grid, i+1, j+1)
  count += maxRegionRecursive(grid, i+1, j) 
  count += maxRegionRecursive(grid, i+1, j-1)
  count += maxRegionRecursive(grid, i, j-1)
  count += maxRegionRecursive(grid, i-1, j-1)
  count += maxRegionRecursive(grid, i-1, j)
  count += maxRegionRecursive(grid, i-1, j+1)
  
  return count
