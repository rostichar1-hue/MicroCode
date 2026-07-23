def group_by(rows, group_field, agg_field, agg_type='avg'):
    groups = {}
    for row in rows:
        key = row.get(group_field)
        val = row.get(agg_field)
        if key not in groups:
            groups[key] = []
        groups[key].append(val)

    result = []
    for key, vals in groups.items():
        if agg_type == 'avg':
            result.append({group_field: key, f'avg_{agg_field}': sum(vals)/len(vals)})
        elif agg_type == 'sum':
            result.append({group_field: key, f'sum_{agg_field}': sum(vals)})
        elif agg_type == 'count':
            result.append({group_field: key, f'count_{agg_field}': len(vals)})
    return result
