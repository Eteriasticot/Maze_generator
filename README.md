# Maze generator
Just a <ins>maze generator</ins> in python. Ideally I'd like to generate different kinds of maze.

## Perfect maze
First of all, we need to define what a perfect maze is. A perfect maze must always have a single path between two of its points. This means a perfect maze can't have isolated areas and can't have any loop.
For example, this is a perfect maze:

![Perfect_Maze](https://github.com/user-attachments/assets/c1b779ed-7805-4ea5-ac77-61929b7e798c)

## Algorythm
I used [CaptainLuma](https://www.youtube.com/@captainluma7991)'s maze generation algorithm to make this program. This algorithm is not the fastest but you can stop the algorithm at any point and it will result into a perfect maze and based on the maze's structure, a simple transformation can give you the path between any two points.

This algorithm works by editing a perfect maze, so all it needs to start is an initial configuration that will always be a perfect maze, no matter the size. To make sure our maze is perfect, we take a grid of nodes. Each node except one will point to a direction, either up, down, left or right. The idea is that if you start from any point and follow the arrows from point to point, you will end up on the only point that points nowhere, the "origin" of the maze. It looks like this:

![Perfect_maze_path](https://github.com/user-attachments/assets/77c61e63-17b4-46c9-81e0-9f278e82f108)
