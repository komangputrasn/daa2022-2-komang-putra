# mahasiswa = ['komang', '2021071015', 'informatika', 'desain dan analisis algoritma', '14 september 2022', 'universitas pembangunan jaya']
# for item in mahasiswa:
#     print(item)

import random
import math

ls = [random.randrange(100) for _ in range(10)]
best_min = ls[0]

for item in ls:
    best_min = max(best_min, item)

print(best_min)