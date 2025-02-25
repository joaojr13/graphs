def relax(u, v, w):
    if v['d'] > u['d'] + w :
        v['d'] = u['d'] + w
        v['pi'] = u
        return True
    return False