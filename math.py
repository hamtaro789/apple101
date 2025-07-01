import random

# กำหนดค่าที่ใช้ได้
values = [1000 * i for i in range(1, 11)]  # [1000, 2000, ..., 10000]
target_sum = 400000
num_values = 60

# ฟังก์ชันสุ่มแบบมีเงื่อนไขให้ผลรวม = 400,000
def generate_random_combination(values, num_values, target_sum, max_attempts=100000):
    for _ in range(max_attempts):
        combo = [random.choice(values) for _ in range(num_values)]
        if sum(combo) == target_sum:
            return combo
    return None

# เรียกใช้ฟังก์ชัน
result = generate_random_combination(values, num_values, target_sum)

if result:
    print("✅ เจอลำดับที่ผลรวม = 400,000 สำเร็จ!")
    print("ตัวเลข:", result)
    print("ผลรวม:", sum(result))
    print("จำนวนแต่ละค่า:", {val: result.count(val) for val in values})
else:
    print("❌ ไม่สามารถหาลำดับที่ผลรวม = 400,000 ได้ในรอบที่กำหนด")