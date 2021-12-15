def sequential_map(*args):
    result = args[-1]
    for function in args[:-1]:
        result = [function(i) for i in result]
    return result

def consensus_filter(*args):
    container = args[-1]
    for function in args[:-1]:
        container = [value for value in container if function(value)]
    return container
