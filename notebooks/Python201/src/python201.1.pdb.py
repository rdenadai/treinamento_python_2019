import pdb


def debugger_old_way(x, y):
    z = x + y
    pdb.set_trace()
    z = z**2
    return z


def debugger_new_way(x, y):
    z = x + y
    breakpoint()
    z = z**2
    return z


# debugger_old_way(10, 2)

debugger_new_way(10, 2)

