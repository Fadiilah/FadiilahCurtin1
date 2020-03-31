import Maze 


def view(grid):
	for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == Maze.EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == Maze.WALL:
                print("I WANT TO", end = "")
                    
            elif grid[i][j] == Maze.START:
                print("GO", end = "")
                    
            elif grid[i][j] == Maze.END:
                print("TO", end = "")
                    
            elif grid[i][j] == Maze.VISITED:
                print("UNIVERSITY", end = "")
                    
            else:
                raise AssertionError
            
        print()
