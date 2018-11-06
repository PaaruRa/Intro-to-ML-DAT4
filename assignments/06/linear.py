class LinearRegression:
    def __init__(self):
        self.coef_ = None

    def fit(X, y):
        """Calculate coefficients from given data.

        The calculated coefficients (including the intercept term)
        are stored in `coef_`.

        Parameters
        ----------
        X: ndarray
            2D numpy array. Each row is an training input.
            Each column is a feature.
        y: ndarray
            2D numpy array. Each row contains a single value which is the output 
            for the corresponding training input.
        """
        # Your Code Here

        # Note: You need to add a column of 1s yourself to the input corresponding to \beta_{0}

        # Use the normal equation to calculate the coefficients i.e betas
        pass

    def predict(X):
        """Make predictions for given input.

        Parameters
        ----------
        X: ndarray
            2D numpy array. Each row is an training input.
            Each column is a feature.

        Returns
        -------
        ndarray
            predictions for each input
        """
        # Your Code Here

        # Note: You need to add a column of 1s yourself to the input corresponding to \beta_{0}
        pass
