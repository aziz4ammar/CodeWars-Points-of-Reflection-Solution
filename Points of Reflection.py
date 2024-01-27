def symmetric_point(p, q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    fx = q[0] + dx
    fy = q[1] + dy
    return [fx, fy]