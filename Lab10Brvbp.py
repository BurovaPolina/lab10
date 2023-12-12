import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Крестики нолики")
root.geometry("250x270+450+150")
root.resizable(False, False)

font = "Georgia 15"

button_list = ["1 1", "1 2", "1 3", "2 1",
               "2 2", "2 3", "3 1", "3 2", "3 3"]
button_in_use = {"1 1": "", "1 2": "", "1 3": "",
                 "2 1": "", "2 2": "", '2 3': "",
                 "3 1": "", "3 2": "", '3 3': ""}
button_y_coordinate = -90
x = -1
button_x_coordinates = [5, 87, 169]

move_counter = 0
field_matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def computer_play():
    for mark in ["O", "☓"]:
        for i in range(3):
            vertical_check = [field_matrix[i][0], field_matrix[i][1], field_matrix[i][2]]
            horizontal_check = [field_matrix[0][i], field_matrix[1][i], field_matrix[2][i]]
            main_diagonale_check = [field_matrix[0][0], field_matrix[1][1], field_matrix[2][2]]
            sub_diagonale_check = [field_matrix[2][0], field_matrix[1][1], field_matrix[0][2]]

            if vertical_check.count(mark) == 2 and vertical_check.count("-") == 1:
                return [i, vertical_check.index("-")]

            if horizontal_check.count(mark) == 2 and horizontal_check.count("-") == 1:
                return [horizontal_check.index("-"), i]

            if main_diagonale_check.count(mark) == 2 and main_diagonale_check.count("-") == 1:
                return [main_diagonale_check.index("-"), main_diagonale_check.index("-")]
            if sub_diagonale_check.count(mark) == 2 and sub_diagonale_check.count("-") == 1:
                if sub_diagonale_check.index("-") == 0:
                    return [2, 0]
                if sub_diagonale_check.index("-") == 1:
                    return [1, 1]
                if sub_diagonale_check.index("-") == 2:
                    return [0, 2]

    if field_matrix[1][1] == "-":
        return [1, 1]
    else:
        for int_i in range(3):
            for int_j in range(3):
                if field_matrix[int_j][int_i] == "-":
                    return [int_j, int_i]


def end_game(mark):
    global field_matrix
    global move_counter
    if check_end(mark)[0]:
        showinfo("", check_end(mark)[1])
        field_matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

        for button_num in range(len(button_list)):
            button_in_use[button_list[button_num]].config(text="")
            move_counter = 0
        return True
    else:
        return False


def check_end(mark):
    for i in range(3):
        if (field_matrix[i][0] == field_matrix[i][1] == field_matrix[i][2] != "-") or (
                field_matrix[0][i] == field_matrix[1][i] == field_matrix[2][i] != "-"):
            return [True, "Победа " + mark]
        elif (field_matrix[0][0] == field_matrix[1][1] == field_matrix[2][2] != "-") or (
                field_matrix[2][0] == field_matrix[1][1] == field_matrix[0][2] != "-"):
            return [True, "Победа " + mark]
    if move_counter == 9:
        return [True, "Ничья"]
    return [False, "Заново"]


def move_calc(button):
    key_coord = list(button_in_use.keys())[list(button_in_use.values()).index(button)]
    coordinate_list = key_coord.split(' ')

    global field_matrix
    global move_counter

    if field_matrix[int(coordinate_list[0]) - 1][int(coordinate_list[1]) - 1] == "-":
        move_counter += 1
        button["text"], mark = "☓", "игрока"
        field_matrix[int(coordinate_list[0]) - 1][int(coordinate_list[1]) - 1] = button["text"]

        if not end_game(mark):
            move_counter += 1
            button_bot = computer_play()
            button_in_use[str(button_bot[0] + 1) + " " + str(button_bot[1] + 1)]["text"], mark = "O", "компьютера"
            field_matrix[button_bot[0]][button_bot[1]] = \
                button_in_use[str(button_bot[0] + 1) + " " + str(button_bot[1] + 1)]["text"]

        end_game(mark)


for button_num in range(len(button_list)):
    x += 1
    if button_num % 3 == 0:
        button_y_coordinate += 90
        x = 0
    button_in_use[button_list[button_num]] = tk.Button(root)
    button_in_use[button_list[button_num]].config(height=3, width=6, font=font,
                                                  command=lambda m=button_in_use[button_list[button_num]]: move_calc(m))
    button_in_use[button_list[button_num]].place(x=button_x_coordinates[x], y=button_y_coordinate)
root.mainloop()
