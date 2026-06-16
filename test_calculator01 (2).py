def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Test functions - pytest จะรู้ว่านี่คือ test เพราะขึ้นต้นด้วย test_
def test_add():
    assert add(3, 5) == 8  # เปลี่ยนจาก 8 เป็น 99

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(4, 5) == 20