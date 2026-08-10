def solution(data, ext, val_ext, sort_by):
    idx_dict = {"code":0, "date":1, "maximum":2, "remain":3}
    return sorted([d for d in data if d[idx_dict[ext]]<val_ext],key=lambda x : x[idx_dict[sort_by]])
