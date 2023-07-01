def data_reverse(data):
    inter, res = [], []
    for bit in range(0, len(data), 8):
        inter.append(data[bit:bit + 8])
    inter = inter[::-1]
    for octet in inter:
        res += octet
    return res
