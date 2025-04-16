import random

class MutationEngine:
    def __init__(self):
        self.mutations = ['nop', 'xor', 'xchg']

    def mutate(self, payload):
        mutations = []
        for mutation_type in self.mutations:
            if mutation_type == 'nop':
                mutations.append(b"\x90" * random.randint(10, 20))
            elif mutation_type == 'xor':
                mutations.append(b"\x31\xD2\xA3")
            elif mutation_type == 'xchg':
                mutations.append(b"\x90\x66\x87\xF6")
        mutations.append(b"\x48\x31\xC9\x48\x81\xE9\xFD\xFF\xFF")
        random.shuffle(mutations)
        return b''.join(mutations) + payload

mutator = MutationEngine()
