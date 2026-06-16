import requests

def test_get_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )
    assert response.status_code == 200
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"User: {data['name']}")
    assert data['id'] == 1
    assert 'name' in data
    assert 'email' in data
    print("API ทำงานถูกต้อง! ✓")

def test_create_post():
    new_post = {
        "title": "ทดสอบ API",
        "body": "นี่คือการทดสอบ POST request",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post
    )
    # ✅ เพิ่มส่วนนี้กลับมา
    assert response.status_code == 201
    data = response.json()
    print(f"สร้าง post ID: {data['id']}")
    assert data['title'] == "ทดสอบ API"
    assert data['userId'] == 1
    print("สร้างข้อมูลสำเร็จ! ✓")

def test_update_post():
    updated_post = {
        "title": "อัพเดทแล้ว",
        "body": "เนื้อหาใหม่",
        "userId": 1
    }
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=updated_post
    )
    assert response.status_code == 200
    data = response.json()
    print(f"Status: {response.status_code}")
    print(f"Title ใหม่: {data['title']}")
    assert data['title'] == "อัพเดทแล้ว"
    print("อัพเดทสำเร็จ! ✓")

def test_delete_post():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    # ✅ เหลือแค่นี้พอ
    assert response.status_code == 200
    print(f"Status: {response.status_code}")
    print("ลบข้อมูลสำเร็จ! ✓")