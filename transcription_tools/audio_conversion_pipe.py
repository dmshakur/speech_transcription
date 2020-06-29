
class Audio_Conversion_Pipe:
    def __init__(self, pipe, v = False):
        self.pipe = pipe
        self.output = None
        self.v = v
    def run(self, first_arg):
        self.output = first_arg
        for node in self.pipe:
            if self.v: print('current node: ', type(node))
            self.output = node.run(self.output)
        if self.v: print('pipe complete, returning output...')
        return self.output