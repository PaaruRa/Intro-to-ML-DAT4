class Series:
    """One-dimensional named array.

    Basically, a "smart" array.

    Parameters
    ----------
    values: list
        list of data values 

    name: str
        name of the Series
    """
    def __init__(self, values, name=None):
        # Code Here
        pass

    def mean(self):
        # Code Here
        pass


class DataFrame:
    """Two-dimensional tabular data structure.

    Basically, a dictionary of `Series` objects.

    Parameters
    ----------
    data_dict: dict
        dictionary of lists. The key is the column name.
        So, dict['col'] is a list of values for the 'col' column
        of the DataFrame.
    """
    def __init__(self, data_dict):
        # Code Here
        pass
