def difference(*args):
    if not args:
        return 0
    max_val = max(args)
    min_val = min(args)
    return round(max_val - min_val, 2)

# Перевірка різниці між максимумом і мінімумом
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'