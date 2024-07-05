i1 = []
i2 = []
i3 = []
i4 = []
i5 = []


def main():
    given = input("Enter Your Name =\t").upper()
    given = list(given)
    col = (len(given) * 6) + 5
    checkLetter(given,col)


def checkLetter(given,col):
    for i in range(len(given)):
        if given[i] == "A":
            A_letter(n=i)
        elif given[i] == "B":
            B_letter(n=i)
        elif given[i] == "C":
            C_letter(n=i)
        elif given[i] == "D":
            D_letter(n=i)
        elif given[i] == "E":
            E_letter(n=i)
        elif given[i] == "F":
            F_letter(n=i)
        elif given[i] == "G":
            G_letter(n=i)
        elif given[i] == "H":
            H_letter(n=i)
        elif given[i] == "I":
            I_letter(n=i)
        elif given[i] == "J":
            J_letter(n=i)
        elif given[i] == "K":
            K_letter(n=i)
        elif given[i] == "L":
            L_letter(n=i)
        elif given[i] == "M":
            M_letter(n=i)
        elif given[i] == "N":
            N_letter(n=i)
        elif given[i] == "O":
            O_letter(n=i)
        elif given[i] == "P":
            P_letter(n=i)
        elif given[i] == "Q":
            Q_letter(n=i)
        elif given[i] == "R":
            R_letter(n=i)
        elif given[i] == "S":
            S_letter(n=i)
        elif given[i] == "T":
            T_letter(n=i)
        elif given[i] == "U":
            U_letter(n=i)
        elif given[i] == "V":
            V_letter(n=i)
        elif given[i] == "W":
            W_letter(n=i)
        elif given[i] == "X":
            X_letter(n=i)
        elif given[i] == "Y":
            Y_letter(n=i)
        elif given[i] == "Z":
            Z_letter(n=i)
        elif given[i] == "1":
            _1_number(n=i)
        elif given[i] == "2":
            _2_number(n=i)
        elif given[i] == "3":
            _3_number(n=i)
        elif given[i] == "4":
            _4_number(n=i)
        elif given[i] == "5":
            _5_number(n=i)
        elif given[i] == "6":
            _6_number(n=i)
        elif given[i] == "7":
            _7_number(n=i)
        elif given[i] == "8":
            _8_number(n=i)
        elif given[i] == "9":
            _9_number(n=i)
        elif given[i] == "0":
            _0_number(n=i)
        elif given[i] == " ":
            space_on(n=i)
        elif given[i] == ".":
            _dot_number(n=i)
        else:
            continue
    Write(i1, i2, i3, i4, i5, col)


def assigner(c1, c2, c3, c4, c5, n):
    if n == 0:
        i1.extend(c1)
        i2.extend(c2)
        i3.extend(c3)
        i4.extend(c4)
        i5.extend(c5)
    else:
        c1 = adder(c1, n)
        c2 = adder(c2, n)
        c3 = adder(c3, n)
        c4 = adder(c4, n)
        c5 = adder(c5, n)
        i1.extend(c1)
        i2.extend(c2)
        i3.extend(c3)
        i4.extend(c4)
        i5.extend(c5)


def Write(i1, i2, i3, i4, i5, col):
    print("\nCHOOSE YOUR CHARACTER\n")
    char = input("ENTER THE SYMBOL = ")
    for i in range(5):
        for j in range(col):
            if i == 0 and j in set(i1):
                print("{:2s}".format(char), end="")
            elif i == 1 and j in set(i2):
                print("{:2s}".format(char), end="")
            elif i == 2 and j in set(i3):
                print("{:2s}".format(char), end="")
            elif i == 3 and j in set(i4):
                print("{:2s}".format(char), end="")
            elif i == 4 and j in set(i5):
                print("{:2s}".format(char), end="")
            else:
                print("{:2s}".format(" "), end="")
        print()
    print()


def A_letter(n):
    li_A_IF1 = [2]
    li_A_IF2 = [1, 3]
    li_A_IF3 = [0, 4]
    li_A_IF4 = [0, 1, 2, 3, 4]
    li_A_IF5 = [0, 4]
    # n = n + 1
    assigner(li_A_IF1, li_A_IF2, li_A_IF3, li_A_IF4, li_A_IF5, n)


def B_letter(n):
    li_B_IF1 = [0, 1, 2, 3]
    li_B_IF2 = [0, 4]
    li_B_IF3 = [0, 1, 2, 3]
    li_B_IF4 = [0, 4]
    li_B_IF5 = [0, 1, 2, 3]
    # n = n + 1
    assigner(li_B_IF1, li_B_IF2, li_B_IF3, li_B_IF4, li_B_IF5, n)


def C_letter(n):
    li_C_IF1 = [2, 3, 4]
    li_C_IF2 = [1]
    li_C_IF3 = [0]
    li_C_IF4 = [1]
    li_C_IF5 = [2, 3, 4]
    # n = n + 1
    assigner(li_C_IF1, li_C_IF2, li_C_IF3, li_C_IF4, li_C_IF5, n)


def D_letter(n):
    li_D_IF1 = [0, 1, 2]
    li_D_IF2 = [1, 3]
    li_D_IF3 = [1, 4]
    li_D_IF4 = [1, 3]
    li_D_IF5 = [0, 1, 2]
    # n = n + 1
    assigner(li_D_IF1, li_D_IF2, li_D_IF3, li_D_IF4, li_D_IF5, n)


def E_letter(n):
    li_E_IF1 = [0, 1, 2, 3, 4]
    li_E_IF2 = [0]
    li_E_IF3 = [0, 1, 2, 3, 4]
    li_E_IF4 = [0]
    li_E_IF5 = [0, 1, 2, 3, 4]
    # n = n + 1
    assigner(li_E_IF1, li_E_IF2, li_E_IF3, li_E_IF4, li_E_IF5, n)


def F_letter(n):
    li_F_IF1 = [0, 1, 2, 3, 4]
    li_F_IF2 = [0]
    li_F_IF3 = [0, 1, 2, 3, 4]
    li_F_IF4 = [0]
    li_F_IF5 = [0]
    # n = n + 1
    assigner(li_F_IF1, li_F_IF2, li_F_IF3, li_F_IF4, li_F_IF5, n)


def G_letter(n):
    li_G_IF1 = [0, 1, 2, 3, 4]
    li_G_IF2 = [0]
    li_G_IF3 = [0, 2, 3, 4]
    li_G_IF4 = [0, 4]
    li_G_IF5 = [0, 1, 2, 3, 4]
    # n = n + 1
    assigner(li_G_IF1, li_G_IF2, li_G_IF3, li_G_IF4, li_G_IF5, n)


def H_letter(n):
    li_H_IF1 = [0, 4]
    li_H_IF2 = [0, 4]
    li_H_IF3 = [0, 1, 2, 3, 4]
    li_H_IF4 = [0, 4]
    li_H_IF5 = [0, 4]
    # n = n + 1
    assigner(li_H_IF1, li_H_IF2, li_H_IF3, li_H_IF4, li_H_IF5, n)


def I_letter(n):
    li_I_IF1 = [0, 1, 2, 3, 4]
    li_I_IF2 = [2]
    li_I_IF3 = [2]
    li_I_IF4 = [2]
    li_I_IF5 = [0, 1, 2, 3, 4]
    # n = n + 1
    assigner(li_I_IF1, li_I_IF2, li_I_IF3, li_I_IF4, li_I_IF5, n)


def J_letter(n):
    li_J_IF1 = [0, 1, 2, 3, 4]
    li_J_IF2 = [2]
    li_J_IF3 = [2]
    li_J_IF4 = [2]
    li_J_IF5 = [0, 1, 2]
    # n = n + 1
    assigner(li_J_IF1, li_J_IF2, li_J_IF3, li_J_IF4, li_J_IF5, n)


def K_letter(n):
    li_K_IF1 = [0, 4]
    li_K_IF2 = [0, 3]
    li_K_IF3 = [0, 1, 2]
    li_K_IF4 = [0, 3]
    li_K_IF5 = [0, 4]
    # n = n + 1
    assigner(li_K_IF1, li_K_IF2, li_K_IF3, li_K_IF4, li_K_IF5, n)


def L_letter(n):
    li_L_IF1 = [0]
    li_L_IF2 = [0]
    li_L_IF3 = [0]
    li_L_IF4 = [0]
    li_L_IF5 = [0, 1, 2, 3, 4]
    # n = n + 1
    assigner(li_L_IF1, li_L_IF2, li_L_IF3, li_L_IF4, li_L_IF5, n)


def M_letter(n):
    li_L_IF1 = [0, 4]
    li_L_IF2 = [0, 1, 3, 4]
    li_L_IF3 = [0, 2, 4]
    li_L_IF4 = [0, 4]
    li_L_IF5 = [0, 4]
    # n = n + 1
    assigner(li_L_IF1, li_L_IF2, li_L_IF3, li_L_IF4, li_L_IF5, n)


def N_letter(n):
    li_N_IF1 = [0, 4]
    li_N_IF2 = [0, 1, 4]
    li_N_IF3 = [0, 2, 4]
    li_N_IF4 = [0, 3, 4]
    li_N_IF5 = [0, 4]
    # n = n + 1
    assigner(li_N_IF1, li_N_IF2, li_N_IF3, li_N_IF4, li_N_IF5, n)


def O_letter(n):
    li_O_IF1 = [1, 2, 3]
    li_O_IF2 = [0, 4]
    li_O_IF3 = [0, 4]
    li_O_IF4 = [0, 4]
    li_O_IF5 = [2, 3, 1]
    # n = n + 1
    assigner(li_O_IF1, li_O_IF2, li_O_IF3, li_O_IF4, li_O_IF5, n)


def P_letter(n):
    li_P_IF1 = [0, 1, 2, 3]
    li_P_IF2 = [0, 4]
    li_P_IF3 = [0, 1, 2, 3]
    li_P_IF4 = [0]
    li_P_IF5 = [0]
    # n = n + 1
    assigner(li_P_IF1, li_P_IF2, li_P_IF3, li_P_IF4, li_P_IF5, n)


def Q_letter(n):
    li_Q_IF1 = [2]
    li_Q_IF2 = [1, 3]
    li_Q_IF3 = [0, 4]
    li_Q_IF4 = [1, 3]
    li_Q_IF5 = [2, 4]
    # n = n + 1
    assigner(li_Q_IF1, li_Q_IF2, li_Q_IF3, li_Q_IF4, li_Q_IF5, n)


def R_letter(n):
    li_R_IF1 = [0, 1, 2, 3]
    li_R_IF2 = [0, 4]
    li_R_IF3 = [0, 1, 2, 3]
    li_R_IF4 = [0, 3]
    li_R_IF5 = [0, 4]
    # n = n + 1
    assigner(li_R_IF1, li_R_IF2, li_R_IF3, li_R_IF4, li_R_IF5, n)


def S_letter(n):
    li_E_IF1 = [1, 2, 3, 4]
    li_E_IF2 = [0]
    li_E_IF3 = [1, 2, 3]
    li_E_IF4 = [4]
    li_E_IF5 = [0, 1, 2, 3]
    # n = n + 1
    assigner(li_E_IF1, li_E_IF2, li_E_IF3, li_E_IF4, li_E_IF5, n)


def T_letter(n):
    li_T_IF1 = [0, 1, 2, 3, 4]
    li_T_IF2 = [2]
    li_T_IF3 = [2]
    li_T_IF4 = [2]
    li_T_IF5 = [2]
    # n = n + 1
    assigner(li_T_IF1, li_T_IF2, li_T_IF3, li_T_IF4, li_T_IF5, n)


def U_letter(n):
    li_V_IF1 = [0, 4]
    li_V_IF2 = [0, 4]
    li_V_IF3 = [0, 4]
    li_V_IF4 = [0, 4]
    li_V_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_V_IF1, li_V_IF2, li_V_IF3, li_V_IF4, li_V_IF5, n)


def V_letter(n):
    li_U_IF1 = [0, 4]
    li_U_IF2 = [0, 4]
    li_U_IF3 = [0, 4]
    li_U_IF4 = [1, 3]
    li_U_IF5 = [2]
    # n = n + 1
    assigner(li_U_IF1, li_U_IF2, li_U_IF3, li_U_IF4, li_U_IF5, n)


def W_letter(n):
    li_W_IF1 = [0, 4]
    li_W_IF2 = [0, 4]
    li_W_IF3 = [0, 2, 4]
    li_W_IF4 = [0, 1, 3, 4]
    li_W_IF5 = [0, 4]
    # n = n + 1
    assigner(li_W_IF1, li_W_IF2, li_W_IF3, li_W_IF4, li_W_IF5, n)


def X_letter(n):
    li_X_IF1 = [0, 4]
    li_X_IF2 = [1, 3]
    li_X_IF3 = [2]
    li_X_IF4 = [1, 3]
    li_X_IF5 = [0, 4]
    # n = n + 1
    assigner(li_X_IF1, li_X_IF2, li_X_IF3, li_X_IF4, li_X_IF5, n)


def Y_letter(n):
    li_Y_IF1 = [0, 4]
    li_Y_IF2 = [1, 3]
    li_Y_IF3 = [2]
    li_Y_IF4 = [2]
    li_Y_IF5 = [2]
    # n = n + 1
    assigner(li_Y_IF1, li_Y_IF2, li_Y_IF3, li_Y_IF4, li_Y_IF5, n)


def Z_letter(n):
    li_Z_IF1 = [0, 1, 2, 3, 4]
    li_Z_IF2 = [3]
    li_Z_IF3 = [2]
    li_Z_IF4 = [1]
    li_Z_IF5 = [0, 1, 2, 3, 4]
    # n = n + 1
    assigner(li_Z_IF1, li_Z_IF2, li_Z_IF3, li_Z_IF4, li_Z_IF5, n)


def _1_number(n):
    li_1_IF1 = [2]
    li_1_IF2 = [1, 2]
    li_1_IF3 = [2]
    li_1_IF4 = [2]
    li_1_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_1_IF1, li_1_IF2, li_1_IF3, li_1_IF4, li_1_IF5, n)


def _1_number(n):
    li_1_IF1 = [2]
    li_1_IF2 = [1, 2]
    li_1_IF3 = [2]
    li_1_IF4 = [2]
    li_1_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_1_IF1, li_1_IF2, li_1_IF3, li_1_IF4, li_1_IF5, n)


def _2_number(n):
    li_2_IF1 = [1, 2, 3]
    li_2_IF2 = [1, 3]
    li_2_IF3 = [2]
    li_2_IF4 = [1]
    li_2_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_2_IF1, li_2_IF2, li_2_IF3, li_2_IF4, li_2_IF5, n)


def _3_number(n):
    li_3_IF1 = [1, 2, 3]
    li_3_IF2 = [3]
    li_3_IF3 = [1, 2, 3]
    li_3_IF4 = [3]
    li_3_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_3_IF1, li_3_IF2, li_3_IF3, li_3_IF4, li_3_IF5, n)


def _4_number(n):
    li_4_IF1 = [1, 3]
    li_4_IF2 = [1, 3]
    li_4_IF3 = [1, 2, 3]
    li_4_IF4 = [3]
    li_4_IF5 = [3]
    # n = n + 1
    assigner(li_4_IF1, li_4_IF2, li_4_IF3, li_4_IF4, li_4_IF5, n)


def _5_number(n):
    li_5_IF1 = [1, 2, 3]
    li_5_IF2 = [1]
    li_5_IF3 = [1, 2, 3]
    li_5_IF4 = [3]
    li_5_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_5_IF1, li_5_IF2, li_5_IF3, li_5_IF4, li_5_IF5, n)


def _6_number(n):
    li_6_IF1 = [1, 2, 3]
    li_6_IF2 = [1]
    li_6_IF3 = [1, 2, 3]
    li_6_IF4 = [1, 3]
    li_6_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_6_IF1, li_6_IF2, li_6_IF3, li_6_IF4, li_6_IF5, n)


def _7_number(n):
    li_7_IF1 = [0, 1, 2, 3]
    li_7_IF2 = [3]
    li_7_IF3 = [2]
    li_7_IF4 = [1]
    li_7_IF5 = [0]
    # n = n + 1
    assigner(li_7_IF1, li_7_IF2, li_7_IF3, li_7_IF4, li_7_IF5, n)


def _8_number(n):
    li_8_IF1 = [1, 2, 3]
    li_8_IF2 = [1, 3]
    li_8_IF3 = [1, 3, 2]
    li_8_IF4 = [1, 3]
    li_8_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_8_IF1, li_8_IF2, li_8_IF3, li_8_IF4, li_8_IF5, n)


def _9_number(n):
    li_9_IF1 = [1, 2, 3]
    li_9_IF2 = [1, 3]
    li_9_IF3 = [1, 3, 2]
    li_9_IF4 = [3]
    li_9_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_9_IF1, li_9_IF2, li_9_IF3, li_9_IF4, li_9_IF5, n)


def _0_number(n):
    li_0_IF1 = [1, 2, 3]
    li_0_IF2 = [1, 3]
    li_0_IF3 = [1, 3]
    li_0_IF4 = [1, 3]
    li_0_IF5 = [1, 2, 3]
    # n = n + 1
    assigner(li_0_IF1, li_0_IF2, li_0_IF3, li_0_IF4, li_0_IF5, n)


def _dot_number(n):
    li_9_IF1 = []
    li_9_IF2 = []
    li_9_IF3 = []
    li_9_IF4 = []
    li_9_IF5 = [2]
    # n = n + 1
    assigner(li_9_IF1, li_9_IF2, li_9_IF3, li_9_IF4, li_9_IF5, n)


def space_on(n):
    li_IF1 = []
    li_IF2 = []
    li_IF3 = []
    li_IF4 = []
    li_IF5 = []
    # n = n + 1
    assigner(li_IF1, li_IF2, li_IF3, li_IF4, li_IF5, n)


def adder(element, n):
    li = []
    for i in element:
        i += 6 * n
        li.append(i)
    return li


if __name__ == "__main__":
    print(__name__)
    main()
