markers_x_set = {(1, 2), (2, 1), (3, 1), (2, 2), (1, 3)}
wins = [
    # Horizontal wins
    {(1,1),(2,1),(3,1)},
    {(1,2), (2,2),(3,2)},
    {(1,3), (2,3), (3,3)},
    # Vertical wins
    {(1,1),(1,2),(1,3)},
    {(2,1),(2,2),(2,3)},
    {(3,1),(3,2),(3,3)},
    # Diagonal wins
    {(1,1),(2,2),(3,3)},
    {(1,3),(2,2),(3,1)}
]

for win in wins:
    x_win = win.issubset(markers_x_set)
    print(x_win)