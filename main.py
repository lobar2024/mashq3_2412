# 1) 1–10 sonlarning kublari
tuple1 = tuple(i**3 for i in range(1, 11))

# 2) nums ichidan toq sonlar
nums = [2, 5, 7, 8]
tuple2 = tuple(i for i in nums if i % 2 != 0)

# 3) "python" harflarining ASCII kodi
tuple3 = tuple(ord(ch) for ch in "python")

# 4) sonlarning 2 barobari
nums2 = [1, 2, 3, 4]
tuple4 = tuple(i * 2 for i in nums2)

print(tuple1, tuple2, tuple3, tuple4)
