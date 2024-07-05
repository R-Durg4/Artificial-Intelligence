graph = eval(input("Enter your graph as a dictionary: "))
print("\nThe graph you entered is:")
for k, v in graph.items():
    print(k, ":", v)

start = input("\nEnter the start node: ")
goal = input("Enter the goal node: ")
heuristics = eval(input("\nEnter the heuristics as a dictionary: "))

def a_star(graph, start, goal, heuristics):
    open_set = set([start])
    closed_set = set()
    g = {start: 0}
    parents = {start: start}

    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristics[x])

        if n == goal:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("\nPath found:", path)
            return

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in graph.get(n, []):
            if m in closed_set:
                continue

            tentative_g = g[n] + weight

            if m not in open_set:
                open_set.add(m)
            elif tentative_g >= g[m]:
                continue

            parents[m] = n
            g[m] = tentative_g

    print("Path does not exist!")

a_star(graph, start, goal, heuristics)
