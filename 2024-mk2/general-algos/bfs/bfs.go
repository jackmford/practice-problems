
package main

import "fmt"

type Graph struct {
  vertices map[int][]int // key: vertex, value: list of connected vertices
}

// AddEdge adds an edge from vertex u to vertex v in the graph
func (g *Graph) AddEdge(u, v int) {
  if g.vertices == nil {
    g.vertices = make(map[int][]int)
  }

  g.vertices[u] = append(g.vertices[u], v)
  g.vertices[v] = append(g.vertices[v], u) // Assuming undirected
}

func (g *Graph) BFS(start int) {
  // create a visited map
  visited := make(map[int]bool)

  // create a queue
  q := []int{}
  q = append(q, start)
  // while the queue is not empty, get current node
  for len(q) > 0 {
    cur := q[0]
    q = q[1:]

    fmt.Println(cur)
    visited[cur] = true

    for _, neighbor := range g.vertices[cur] {
      if !visited[neighbor] {
        q = append(q, neighbor)
      }
    }
  }

  // loop it's neighbors, if they aren't visited add them and visit them
}

func main() {
  graph := &Graph{}
  graph.AddEdge(0, 1)
  graph.AddEdge(0, 2)
  graph.AddEdge(1, 3)
  graph.AddEdge(1, 4)
  graph.AddEdge(2, 5)
  graph.AddEdge(2, 6)

  graph.BFS(0)
}
