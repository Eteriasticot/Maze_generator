import Maze as M

if __name__ == "__main__":
    n = 400
    m = 400
    
    image = M.o_im_path(n, m)
    M.im_plot(image)