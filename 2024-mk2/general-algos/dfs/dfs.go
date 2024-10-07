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

func (g *Graph) DFS(start int, visited map[int]bool) {
  visited[start] = true

  fmt.Println(start)
  for _, neighbor := range g.vertices[start] {
    if !visited[neighbor] {
      g.DFS(neighbor, visited)
    }
  }
}

func main() {
  visited := make(map[int]bool)
  graph := &Graph{}
  graph.AddEdge(0, 1)
  graph.AddEdge(0, 2)
  graph.AddEdge(1, 3)
  graph.AddEdge(1, 4)
  graph.AddEdge(2, 5)
  graph.AddEdge(2, 6)


  graph.DFS(0, visited)
}
