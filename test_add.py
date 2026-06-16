def add(a, b):
    return a + b

expected = 10
actual = add(3, 5)

if actual == expected:
    print("PASS ✓")
else:
    print(f"FAIL ✗ — expected {expected} but got {actual}")