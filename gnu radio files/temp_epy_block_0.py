import numpy as np
from gnuradio import gr

class bit_stream_generator(gr.sync_block):
    """
    Custom block to generate a bit stream.
    """
    def __init__(self, bit_pattern="101010", bit_rate=10):
        """
        Initialize the block.
        :param bit_pattern: String of '1's and '0's representing the bit pattern.
        :param bit_rate: Number of bits per second.
        """
        self.bit_pattern = [int(b) for b in bit_pattern]
        self.bit_rate = bit_rate
        self.sample_rate = 10  # Default sample rate in samples/sec.
        self.samples_per_bit = int(self.sample_rate / self.bit_rate)
        
        super().__init__(
            name="bit_stream_generator",
            in_sig=None,
            out_sig=[np.int8]  # Output a stream of bits as 8-bit integers
        )

    def work(self, input_items, output_items):
        """
        Process block logic.
        """
        output = output_items[0]
        num_bits = len(output) // self.samples_per_bit
        bit_sequence = np.tile(self.bit_pattern, num_bits // len(self.bit_pattern) + 1)
        
        for i in range(num_bits):
            output[i * self.samples_per_bit:(i + 1) * self.samples_per_bit] = bit_sequence[i]
        
        return len(output)
