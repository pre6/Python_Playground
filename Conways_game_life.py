import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt




# Creating the grid:

def create_grid():
    '''To crete a random grid, I want around 20% of the numbers to be 1s and 80% to be 0's
    to do this, i need to use np.random.choice'''

    grid = np.random.choice([0,255],(50,50), replace=True, p=[0.80,0.20])
    return grid


def next_generation(frame, img, grid):
    '''Step one: create a copy for our new grid'''
    new_grid = grid.copy()

    '''step two updtae the new grid:'''
    N = grid.shape[0] - 1
    for i in np.arange(grid.shape[0]):
        for j in np.arange(grid.shape[1]):

            total = grid[(i-1)%N,(j-1)%N] + grid[(i-1)%N,j] + grid[(i-1)%N,(j+1)%N] + \
                    grid[i,(j-1)%N] + grid[i,(j+1)%N] + \
                    grid[(i+1)%N,(j-1)%N] + grid[(i+1)%N,j] + grid[(i+1)%N,(j+1)%N]
            
            if (total > 255*3 or total < 255*2) and grid[i,j] == 255:
                new_grid[i,j] = 0
            elif total == 255*3 and grid[i,j] == 0:
                new_grid[i,j] = 255
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,




def total_function():
    grid = create_grid()
    fig,ax = plt.subplots()
    img = ax.imshow(grid)
    ani = animation.FuncAnimation(fig, next_generation, fargs=(img,grid,),
                                  frames=10, save_count=50)
    hello = ani
    
    plt.show()

total_function()
