origin = 0


def position(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


t = position(origin)
print(t(2))
print(t(3))
print(t(5))
