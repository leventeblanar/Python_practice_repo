# graphs are data structures that represent conenctions between nodes

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}

def get_neighbours(graph: dict, node: str) -> list[str]:
    if node not in graph:
        return []
    else:
        return graph[node]

def main():
    print(get_neighbours(graph, "A"))

    print(get_neighbours(graph, "X"))

main()