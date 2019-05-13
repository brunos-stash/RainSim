def side(a,b,c):
    """ Returns a position of the point c relative to the line going through a and b
        Points a, b are expected to be different
    """
    d = (c[1]-a[1])*(b[0]-a[0]) - (b[1]-a[1])*(c[0]-a[0])
    return 1 if d > 0 else (-1 if d < 0 else 0)

def is_point_in_closed_segment(a, b, c):
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a[0] < b[0]:
        return a[0] <= c[0] and c[0] <= b[0]
    if b[0] < a[0]:
        return b[0] <= c[0] and c[0] <= a[0]

    if a[1] < b[1]:
        return a[1] <= c[1] and c[1] <= b[1]
    if b[1] < a[1]:
        return b[1] <= c[1] and c[1] <= a[1]

    return a[0] == c[0] and a[1] == c[1]

#
def closed_segment_intersect(a,b,c,d):
    """ Verifies if closed segments a, b, c, d do intersect.
    """
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a,b,c)
    s2 = side(a,b,d)

    # All points are collinear
    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment(a, b, c) or is_point_in_closed_segment(a, b, d) or \
            is_point_in_closed_segment(c, d, a) or is_point_in_closed_segment(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    s1 = side(c,d,a)
    s2 = side(c,d,b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    return True

if __name__ == "__main__":

    #testcases
    def test(a,b,c,d, explanation):
        print(f'a: {a} | b: {b}')
        print(f'c: {c} | d: {d}')
        print(f'{explanation}: ',closed_segment_intersect(a,b,c,d))
        print('')

    test((1,1),(1,1),(1,1),(1,1), 'same point')
    test((1,10),(1,10),(1,10),(1,20), 'point on vertical line')
    test((1,1),(1,10),(1,1),(1,10), 'same line')
    test((1,1),(1,10),(1,1),(1,100), 'line on longer vertical line')
    test((1,1),(1,10),(2,1),(2,100), 'line parallel to longer vertical line')