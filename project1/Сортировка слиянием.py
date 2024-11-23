def merge(a, b):
    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[i]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c + a[i:] + b[j:]


def merge_sort(a):
    if len(a) <= 1:
        return a
    i = len(a) // 2
    return merge(merge_sort(a[:i]), merge_sort(a[:i]))
