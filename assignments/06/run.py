from linear import LinearRegression


def main():
    inputs = np.array([[2., 5.],
                       [3., 4.],
                       [2., 3.],
                       [7., 9.],
                       [1., 4.]
                       ])

    # Let b0 = 1, b1 = 2, b2 = -1
    outputs = np.array([[0.], # 1 + 2 * 2. + (-1) * 5.
                        [3.], # 1 + 2 * 3. + (-1) * 4.
                        [2.], # 1 + 2 * 2. + (-1) * 3.
                        [6.], # 1 + 2 * 7. + (-1) * 9.
                        [-1.]
                        ]) # 1 + 2 * 1. + (-1) * 4.

    model = LinearRegression()
    model.fit(inputs, outputs)
    print(model.coeffs_) # Should output [[1.], [2.], [-1.]]

    new_inputs = np.array([[5., 1.],
                           [3., 2.],
                           [1., 1.]])

    predictions = model.predict(new_inputs)
    print(predictions) # Should output [[10.], [5.], [2.]]


if __name__ == '__main__':
    main()
