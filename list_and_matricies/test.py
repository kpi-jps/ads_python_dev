Matriz = [[1,2], [3,4], [5,6], [7,8]]
i = 0
while i < len(Matriz):
    print(f"Elementos da linha {i} ")
    j = 0
    while j < len(Matriz[i]):
        print(f"{Matriz[i][j]}")
        j += 1
    i += 1
