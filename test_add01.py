def add(a, b):
    return a + b

expected = 8
actual = add(3, 5)

if actual == expected:
    print("PASS ✓")
else:
    print(f"FAIL ✗ — expected {expected} but got {actual}")