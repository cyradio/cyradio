from cyradio.gnuradio_wrapper import GnuradioBlock

try:
    from gnuradio import gr
    import gnuradio
    using_gnuradio=True
except ImportError:
    using_gnuradio=False


class BlockWrapper(object):
    def __init__(self, block, input_types, output_types):
        self.__block=block
        self.__io_signature = input_types, output_types
        self.__connexions = [[None for _ in i] for i in (input_types, output_types)]

    @property
    def input_types(self):
        return self.__io_signature[0]

    @property
    def output_types(self):
        return self.__io_signature[1]

    @property
    def input_connexions(self):
        return self.__connexions[0]

    @property
    def output_connexions(self):
        return self.__connexions[1]

    def __connect_io(self,connexion,port,input_output):
        if type(connexion) in (list,tuple):
            block, block_port = connexion
        else:
            block = connexion
            block_port=0
        self.__connexions[input_output][port] = block,block_port

    def connect_input(self,source,port):
        self.__connect_io(source,port,0)

    def connect_output(self,source,port):
        self.__connect_io(source,port,1)

class Flowgraph(object):
    def __init__(self):
        self.__blocks = {}

    @staticmethod
    def __parse_connexion(connexion):
        if type(connexion) in (list,tuple):
            block, block_port = connexion
        else:
            block = connexion
            block_port=0

        if using_gnuradio and "gnuradio.blocks" in block.__module__:
            block = GnuradioBlock(block)

        return block,block_port

    def __add_block(self, block):
        self.__blocks[block] = [[None for _ in range(i)] for i in [block.n_inputs, block.n_outputs]]

    def connect(self, *args):
        connexions = [self.__parse_connexion(i) for i in args]
        for start,stop in zip(connexions[:-1],connexions[1:]):
            for b in [start[0],stop[0]]:
                self.__add_block(b)
            self.__blocks[start[0]][1][start[1]] = stop
            self.__blocks[stop[0]][1][stop[1]] = start

    def start(self, async=False):
        pass