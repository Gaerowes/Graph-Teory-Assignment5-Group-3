import networkx as nx
import matplotlib.pyplot as plt


# =========================
# INPUT MATRIX
# =========================

def input_matrix():
    matrix_type = input(
        "Enter matrix type (adjacency/incidence): "
    ).strip().lower()

    if matrix_type not in ("adjacency", "incidence"):
        print("Invalid matrix type.")
        return None, None

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix = []

    print(f"Enter the matrix values, with {columns} values per row:")

    for i in range(rows):
        row = list(map(int, input().split()))

        if len(row) != columns:
            print("Invalid number of values.")
            return None, None

        matrix.append(row)

    print(f"\n{matrix_type.title()} Matrix:")

    for row in matrix:
        print(*row)

    return matrix_type, matrix


# =========================
# ADJACENCY → EDGES
# =========================

def adjacency_to_edges(matrix):
    edges = []

    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                edges.append((i + 1, j + 1))

    return edges


# =========================
# INCIDENCE → EDGES
# =========================

def incidence_to_edges(matrix):
    edges = []

    rows = len(matrix)
    columns = len(matrix[0])

    for j in range(columns):

        vertices = []

        for i in range(rows):
            if matrix[i][j] == 1:
                vertices.append(i + 1)

        if len(vertices) == 2:
            edges.append((vertices[0], vertices[1]))

        else:
            print(
                f"Warning: Edge e{j + 1} "
                f"does not connect exactly 2 vertices."
            )

    return edges


# =========================
# FUNDAMENTAL CYCLE MATRIX
# =========================

def fundamental_cycle_matrix(number_of_vertices, edges):

    graph = nx.Graph()

    graph.add_nodes_from(
        range(1, number_of_vertices + 1)
    )

    graph.add_edges_from(edges)

    # Create spanning tree
    spanning_tree = nx.minimum_spanning_tree(graph)

    tree_edges = set()

    for u, v in spanning_tree.edges():
        tree_edges.add(tuple(sorted((u, v))))

    # Find non-tree edges
    non_tree_edges = []

    for edge in edges:

        normalized_edge = tuple(sorted(edge))

        if normalized_edge not in tree_edges:
            non_tree_edges.append(edge)

    cycles = []

    for extra_edge in non_tree_edges:

        u, v = extra_edge

        path = nx.shortest_path(
            spanning_tree,
            source=u,
            target=v
        )

        cycle_edges = []

        for i in range(len(path) - 1):

            edge = tuple(
                sorted(
                    (path[i], path[i + 1])
                )
            )

            cycle_edges.append(edge)

        cycle_edges.append(
            tuple(sorted(extra_edge))
        )

        cycles.append(cycle_edges)

    matrix = []

    for cycle in cycles:

        row = []

        for edge in edges:

            normalized_edge = tuple(
                sorted(edge)
            )

            if normalized_edge in cycle:
                row.append(1)
            else:
                row.append(0)

        matrix.append(row)

    return matrix, spanning_tree, cycles


# =========================
# CUT-SET MATRIX
# =========================

def cut_set_matrix(number_of_vertices, edges, spanning_tree):

    cut_sets = []

    tree_edges = list(spanning_tree.edges())

    for tree_edge in tree_edges:

        # Copy spanning tree
        temp_tree = spanning_tree.copy()

        # Remove the selected tree edge
        temp_tree.remove_edge(
            tree_edge[0],
            tree_edge[1]
        )

        # Find the two components
        components = list(
            nx.connected_components(temp_tree)
        )

        component_a = components[0]
        component_b = components[1]

        cut_set = []

        # Check every edge in the original graph
        for edge in edges:

            u, v = edge

            if (
                (u in component_a and v in component_b)
                or
                (u in component_b and v in component_a)
            ):
                cut_set.append(
                    tuple(sorted(edge))
                )

        cut_sets.append(cut_set)

    # Create matrix
    matrix = []

    for cut_set in cut_sets:

        row = []

        for edge in edges:

            normalized_edge = tuple(
                sorted(edge)
            )

            if normalized_edge in cut_set:
                row.append(1)
            else:
                row.append(0)

        matrix.append(row)

    return matrix, cut_sets


# =========================
# PRINT FUNDAMENTAL CYCLE
# =========================

def print_fundamental_cycle_matrix(
    matrix,
    edges,
    spanning_tree,
    cycles
):

    print("\n==============================")
    print("FUNDAMENTAL CYCLE MATRIX")
    print("==============================")

    print("     ", end="")

    for i in range(len(edges)):
        print(f"e{i + 1:^4}", end="")

    print()

    for i, row in enumerate(matrix):

        print(f"C{i + 1:<3}", end="")

        for value in row:
            print(f"{value:^5}", end="")

        print()

    print("\nSpanning Tree:")

    tree_edge_list = list(
        spanning_tree.edges()
    )

    for i, edge in enumerate(
        tree_edge_list,
        1
    ):
        print(f"t{i} = {edge}")

    print("\nFundamental Cycles:")

    for i, cycle in enumerate(
        cycles,
        1
    ):

        cycle_labels = []

        for edge in cycle:

            normalized_edge = tuple(
                sorted(edge)
            )

            for j, original_edge in enumerate(
                edges,
                1
            ):

                if (
                    tuple(sorted(original_edge))
                    == normalized_edge
                ):
                    cycle_labels.append(
                        f"e{j}"
                    )

        print(
            f"C{i} = "
            f"{{{', '.join(cycle_labels)}}}"
        )


# =========================
# PRINT CUT-SET MATRIX
# =========================

def print_cut_set_matrix(
    matrix,
    edges,
    cut_sets,
    spanning_tree
):

    print("\n==============================")
    print("CUT-SET MATRIX")
    print("==============================")

    print("     ", end="")

    for i in range(len(edges)):
        print(f"e{i + 1:^4}", end="")

    print()

    for i, row in enumerate(matrix):

        print(f"K{i + 1:<3}", end="")

        for value in row:
            print(f"{value:^5}", end="")

        print()

    print("\nFundamental Cut-Sets:")

    for i, cut_set in enumerate(
        cut_sets,
        1
    ):

        cut_labels = []

        for edge in cut_set:

            normalized_edge = tuple(
                sorted(edge)
            )

            for j, original_edge in enumerate(
                edges,
                1
            ):

                if (
                    tuple(sorted(original_edge))
                    == normalized_edge
                ):
                    cut_labels.append(
                        f"e{j}"
                    )

        print(
            f"K{i} = "
            f"{{{', '.join(cut_labels)}}}"
        )


# =========================
# VISUALIZE GRAPH
# =========================

def visualize_graph(
    number_of_vertices,
    edges
):

    graph = nx.Graph()

    for vertex in range(
        1,
        number_of_vertices + 1
    ):
        graph.add_node(vertex)

    graph.add_edges_from(edges)

    pos = nx.spring_layout(
        graph,
        seed=42
    )

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=1000,
        font_size=12
    )

    edge_labels = {}

    for i, edge in enumerate(
        edges,
        1
    ):
        edge_labels[edge] = f"e{i}"

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels
    )

    plt.title("Graph Visualization")

    plt.show()


# =========================
# MAIN PROGRAM
# =========================

matrix_type, matrix = input_matrix()


if matrix is not None:

    # Convert matrix to edges
    if matrix_type == "adjacency":

        edges = adjacency_to_edges(matrix)

    else:

        edges = incidence_to_edges(matrix)


    # Display edges
    print("\nEdges:")

    for i, edge in enumerate(
        edges,
        1
    ):
        print(
            f"e{i} = ({edge[0]}, {edge[1]})"
        )


    # Fundamental Cycle Matrix
    (
        cycle_matrix,
        spanning_tree,
        cycles
    ) = fundamental_cycle_matrix(
        len(matrix),
        edges
    )

    print_fundamental_cycle_matrix(
        cycle_matrix,
        edges,
        spanning_tree,
        cycles
    )


    # Cut-Set Matrix
    (
        cut_matrix,
        cut_sets
    ) = cut_set_matrix(
        len(matrix),
        edges,
        spanning_tree
    )

    print_cut_set_matrix(
        cut_matrix,
        edges,
        cut_sets,
        spanning_tree
    )


    # Visualize Graph
    visualize_graph(
        len(matrix),
        edges
    )