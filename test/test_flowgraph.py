from unittest import TestCase
from cyradio import Flowgraph

class TestFlowgraph(TestCase):
    def test_gnuradio(self):
        from gnuradio import blocks
        fg = Flowgraph()
        src = blocks.vector_source_f(range(100))
        mul = blocks.multiply_const_ff(2)
        snk = blocks.vector_sink_f()
        fg.connect(src,mul,snk)
        fg.start()
