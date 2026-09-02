"""
[Assignment-2]: Find covarinace matrix of 3 variables
"""


def list_sum(values):
    agg = 0
    for item in values:
        agg += item
    return agg


def calc_mean(values):
    return list_sum(values) / len(values)


def calc_covar(A, B):
    A_mean, B_mean = calc_mean(A), calc_mean(B)

    A_cent = [a - A_mean for a in A]
    B_cent = [b - B_mean for b in B]

    data_len = len(A)
    i = 0
    AB_cent = []
    while i < data_len:
        AB_cent.append(A_cent[i] * B_cent[i])
        i += 1

    covar = list_sum(AB_cent) / (len(AB_cent) - 1)

    return covar


def get_covar_mat(A, B, C):
    covar_AB = calc_covar(A, B)
    covar_AC = calc_covar(A, C)
    covar_BC = calc_covar(B, C)
    var_A = calc_covar(A, A)
    var_B = calc_covar(B, B)
    var_C = calc_covar(C, C)

    covar_mat = [
        [var_A, covar_AB, covar_AC],
        [covar_AB, var_B, covar_BC],
        [covar_AC, covar_BC, var_C],
    ]

    return covar_mat


def take_inputs(attr_name):
    x = input(f"Enter space separated values for attribute {attr_name}:")
    x = x.split(" ")
    x = [float(item) for item in x]

    return x


def display_mat(mat):
    rows = len(mat)
    # cols = len(mat[0])

    for i in range(rows):
        print(" | ".join(map(str, mat[i])))
        print("-------------------")


def main():
    A = take_inputs("A")
    B = take_inputs("B")
    C = take_inputs("C")
    # A = [1, 2, 3]
    # B = [3, 4, 5]
    # C = [4, 4, 10]

    covar_matrix = get_covar_mat(A, B, C)

    display_mat(covar_matrix)


if __name__ == "__main__":
    main()
