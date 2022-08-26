"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Make a new generator, starting at start."""
        self.start_num = start
        self.current_num = self.start_num

    def generate(self):
        self.current_num = self.current_num + 1
        return self.current_num-1

    def reset(self):
        self.current_num = self.start_num