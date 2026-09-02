"""
[Assignment-1]: Find covariance matrix of 2 variables
"""


def calc_mean(values):
    agg = 0
    for item in values:
        agg += item

    return agg / len(values)


def list_sum(values):
    agg = 0
    for item in values:
        agg += item
    return agg


def calc_covar(heights, weights):
    h_mean, w_mean = calc_mean(heights), calc_mean(weights)

    X = [item - h_mean for item in heights]
    Y = [item - w_mean for item in weights]

    X_2 = [item**2 for item in X]
    Y_2 = [item**2 for item in Y]

    data_len = len(heights)
    i = 0
    XY = []
    while i < data_len:
        XY.append(X[i] * Y[i])
        i += 1

    # XY = [x * y for x, y in zip(X, Y)]

    covar_mat = [
        [list_sum(X_2) / (len(X_2) - 1), list_sum(XY) / (len(XY) - 1)],
        [list_sum(XY) / (len(XY) - 1), list_sum(Y_2) / (len(Y_2) - 1)],
    ]

    return covar_mat


def main():
    heights = input("Write space separted heights:")
    weights = input("Write space separeted weights:")

    heights = heights.split(" ")
    weights = weights.split(" ")

    heights = [float(item) for item in heights]
    weights = [float(item) for item in weights]

    # heights = [1.7, 1.62, 1.52, 1.85, 1.91, 1.42]
    # weights = [72, 64, 84, 80, 72, 70]

    res = calc_covar(heights, weights)

    print(res)


if __name__ == "__main__":
    main()
