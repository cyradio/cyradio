class BlockInterface(object):
    not_implemented_error = NotImplementedError("This method must be implemented")

    @property
    def n_inputs(self):
        raise self.not_implemented_error

    @property
    def n_outputs(self):
        raise self.not_implemented_error