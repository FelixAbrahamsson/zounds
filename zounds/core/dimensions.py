class Dimension(object):
    """
    Class representing one dimension of a numpy array, making custom slices
    (e.g., time spans or frequency bands) possible
    """

    def __init__(self):
        super(Dimension, self).__init__()

    def modified_dimension(self, size, windowsize):
        raise NotImplementedError()

    def metaslice(self, index, size):
        return self

    def integer_based_slice(self, index):
        raise NotImplementedError()


class IdentityDimension(Dimension):
    def __init__(self):
        super(IdentityDimension, self).__init__()

    def modified_dimension(self, size, windowsize):
        if size / windowsize == 1:
            yield IdentityDimension()
        else:
            raise ValueError()

    def integer_based_slice(self, index):
        return index
