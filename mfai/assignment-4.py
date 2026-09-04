"""
[Assignment-4]: Compute Inverse of matrix 3x3
"""


def calc_determinant(m):
    det = (
        m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))
        - m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))
        + m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0]))
    )

    return det


def calc_cofactor(m, rows, cols, i, j):
    vals = []
    for row in range(rows):
        if row == i:
            continue
        for col in range(cols):
            if col == j:
                continue
            vals.append(m[row][col])

    cofactor = (vals[0] * vals[3]) - (vals[1] * vals[2])
    return cofactor


def calc_transpose(m):
    # swap only non diagonals
    temp = m[0][2]
    m[0][2] = m[2][0]
    m[2][0] = temp

    temp = m[0][1]
    m[0][1] = m[1][0]
    m[1][0] = temp

    temp = m[1][2]
    m[1][2] = m[2][1]
    m[2][1] = temp

    return m


def calc_adjoint(m, rows, cols):

    adjoint_mat = []
    for i in range(0, rows):
        adjoint_row = []
        for j in range(0, cols):
            minor = calc_cofactor(m, rows, cols, i, j) * ((-1) ** (i + j))
            adjoint_row.append(minor)
        adjoint_mat.append(adjoint_row)

    return calc_transpose(adjoint_mat)


def calc_inverse(m):
    m_det = calc_determinant(m)
    if m_det == 0:
        print("Inverse does not exist")
        return None

    rows = len(m)
    cols = len(m[0])
    adjoint = calc_adjoint(m, rows, cols)
    inverse = []

    for i in range(rows):
        inv_row = []
        for j in range(cols):
            inv_row.append(adjoint[i][j] / m_det)
        inverse.append(inv_row)

    return inverse


def take_inputs():
    for i in range(1, 4):
        x = input(f"Enter space separated value for row {i}:")
        x = x.split(" ")
        x = [float(item) for item in x]

        yield x


def display_mat(mat):
    rows = len(mat)

    for i in range(rows):
        print(" | ".join(map(str, mat[i])))
        print("-------------------")


def main():
    matrix = [row for row in take_inputs()]

    inverse = calc_inverse(matrix)
    if inverse is not None:
        display_mat(inverse)


if __name__ == "__main__":
    main()
