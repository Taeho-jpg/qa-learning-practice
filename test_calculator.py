import pytest

def add(a, b):
    return a + b

# ทดสอบ add() กับหลายค่าพร้อมกัน
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),      # บวกปกติ
    (0, 0, 0),      # ศูนย์
    (-1, 1, 0),     # ติดลบ
    (100, 200, 300) # เลขใหญ่
])
def test_add(a, b, expected):
    assert add(a, b) == expected