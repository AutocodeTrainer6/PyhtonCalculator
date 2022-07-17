def add(a, b):
  return a + b

def test_add_function():
  assert add(5, 8) == 13

def test_add_function_with_str():
  assert add('5', '8') == '13'
