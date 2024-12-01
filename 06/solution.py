import fileinput


class Signal:
    def __init__(self, signal: list, marker_len: int) -> None:
        self.marker_len = marker_len
        self.idx = marker_len
        self.current = signal[:self.idx]
        self.next = signal[self.idx:]

    def test_signal(self):
        if len(set(self.current)) == self.marker_len:
            return 1
        return 0

    def next_step(self):
        self.current += [self.next.pop(0)]
        self.current.pop(0)
        self.idx += 1

    def walk(self):
        while not self.test_signal():
            self.next_step()
        return self.idx


with open("input.txt") as input:
    signal_str = list(input.read())
    signal_part_1 = Signal(signal_str, marker_len=4)
    signal_part_2 = Signal(signal_str, marker_len=14)

print(f"Part 1 answer is {signal_part_1.walk()}")
print(f"Part 2 answer is {signal_part_2.walk()}")
