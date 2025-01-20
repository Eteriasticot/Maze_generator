# Maze generator
Just a <ins>maze generator</ins> in python. Ideally I'd like to generate different kinds of maze. For now it's only supporting rectangle 2D mazes but I'd like to make it so that it supports circular mazes, 3D parallelepipedic ones, cylindrical ones and ideally even spherical ones. I'm pretty close to having the 3D part work but it feels like I'm lightyears away from figuring out the circular ones and even worse, circular ones.

## Perfect maze
First of all, we need to define what a perfect maze is. A perfect maze must always have a single path between two of its points. This means a perfect maze can't have isolated areas and can't have any loop.
For example, this is a perfect maze:

![Perfect_Maze](https://github.com/user-attachments/assets/c1b779ed-7805-4ea5-ac77-61929b7e798c)

## Algorithm
I used [CaptainLuma](https://www.youtube.com/@captainluma7991)'s maze generation algorithm to make this program. This algorithm is not the fastest but you can stop the algorithm at any point and it will result into a perfect maze and based on the maze's structure, a simple transformation can give you the path between any two points.

This algorithm works by editing a perfect maze, so all it needs to start is an initial configuration that will always be a perfect maze, no matter the size. To make sure our maze is perfect, we take a grid of nodes. Each node except one will point to a direction, either up, down, left or right. The idea is that if you start from any point and follow the arrows from point to point, you will end up on the only point that points nowhere, the "origin" of the maze. It looks like this:

![Perfect_maze_path](https://github.com/user-attachments/assets/77c61e63-17b4-46c9-81e0-9f278e82f108)

Since this algorithm needs a perfect maze to edit, the program needs to be able to make one for every single size. The simplest way to do that is to generate a grid of nodes then calculate adjacencies to know in which directions each node will be able to point. From this structure we make every possible point point to the right, if it can't then we make it point down, and finally if it can't then this node will be the origin of the maze. This is what our initial maze configuration looks like:

![Perfect_maze_init](https://github.com/user-attachments/assets/b31b2888-aacc-45c4-ba4e-0bf33d8f1802)
