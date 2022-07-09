def build_query(cmd, value, file):
    if cmd == 'filter':
        res = list(filter(lambda data: value in data, file))
        return res

    if cmd == 'map':
        res = list(map(lambda data: data.split(' ')[int(value)], file))
        res = '\n'.join(res)
        return res

    if cmd == 'unique':
        res = set(file)
        return res

    if cmd == 'sort':
        res = sorted(file, reverse=value)
        return res

    if cmd == 'limit':
        res = ''.join(file)
        res = res.split('\n')
        res = list(res)[:int(value)]
        print(res)
        res = '\n'.join(res)
        return res
