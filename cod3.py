def input_matrix():
    matrix_type = input("Enter matrix type (adjacency/incidence): ").strip().lower()

    if matrix_type not in ("adjacency", "incidence"):
        print("Invalid matrix type.")
        return

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix = []

    print(f"Enter the matrix values, with {columns} values per row:")
    for i in range(rows):
        row = list(map(int, input().split()))

        if len(row) != columns:
            print("Invalid number of values.")
            return

        matrix.append(row)

    print(f"\n{matrix_type.title()} Matrix:")
    for row in matrix:
        print(*row)


input_matrix()
