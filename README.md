# Dijkstra-Algorithm
A simple dijkstra algorithm for my school project, to find the fastest path from each classes for incoming freshmans,

## For Use
Create a .json file with a graph

eg. for rooms(my school example)

*room_graph.json*
```
{
  "room1": {"room2": 3, "room3": 2},
  "room2": {"room1": 4, "room3": 3},
  "room3": {"room1": 2, "room2": 1},
}
```

then, in line 61:
*main.py*
```
dijkstra_path_finder(graph, x, y)
```

In above x could be the starting point, then, y would be the target

To run dijkstra's algorithm in your specified .json file, in line 6L
*main.py*
```
graph_file = "NAME.json"
```
> Remember to change the directed .json file to your specified .json file

## Credits
