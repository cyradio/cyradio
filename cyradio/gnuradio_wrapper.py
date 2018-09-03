from cyradio.interfaces import BlockInterface


class GnuradioBlock(BlockInterface):
    counter = 0

    def __init__(self,block):
        self.block = block
        self.id = self.counter
        self.counter += 1

    def __hash__(self):
        return "gnuradioBlock" + str(self.id)

    @property
    def n_inputs(self):
        return self.block

    @property
    def n_outputs(self):
        return self.block