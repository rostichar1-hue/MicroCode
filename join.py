def join(left_rows, right_rows, left_key, right_key):
    result = []
    for l in left_rows:
        for r in right_rows:
            if l.get(left_key) == r.get(right_key):
                merged = {**l, **r}
                result.append(merged)
    return result
