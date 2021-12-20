#!python3


ROTATIONS = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, z, -y),

    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (-z, x, -y),

    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, z, y),

    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-z, -x, y),

    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-y, -z, x),

    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (y, -z, -x),
]


def test0():
    c = 1, 2, 3
    x = set(rotation(*c) for rotation in ROTATIONS)
    assert len(x) == 24


if __name__ == '__main__':
    test0()
