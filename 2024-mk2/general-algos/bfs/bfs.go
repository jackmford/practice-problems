
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

  // BFS uses a queue, initialize and add first element
  // Need a way to keep track of visited
  // While the queue has items, look at neighbors, visit if they aren't visited and add to queue

  visited := make(map[int]bool)
  queue := []int{start}
  visited[start] = true

  for len(queue) > 0 {
    cur := queue[0]
    queue = queue[1:]

    fmt.Printf("%d ", cur)

    for _, neighbor := range g.vertices[cur] {
      if !visited[neighbor] {
        queue = append(queue, neighbor)
        visited[neighbor] = true
      }
    }

  }

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
