# Написать такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

transformation = lambda x: x * 1
values = [1, 23, 42, '42', 'asdfg' ]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
    