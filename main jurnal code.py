from LayerOrderedHeap import *
from CartesianSumSelection import *
import random

print("=" * 50)
print("CONTOH 1: Array kecil (mudah diverifikasi)")
print("=" * 50)
A = [1, 3, 5]
B = [2, 4, 6]
k = 4

print(f"Array A: {A}")
print(f"Array B: {B}")
print(f"k (ambil {k} terkecil dari semua A+B)")

# Brute force untuk verifikasi
all_sums = sorted([a+b for a in A for b in B])
print(f"\nSemua kombinasi A+B (brute force): {all_sums}")
print(f"k terkecil (brute force): {sorted(all_sums[:k])}")

css = CartesianSumSelection(A, B)
result = css.select(k)
print(f"k terkecil (CartesianSumSelection): {sorted(result)}")

print("\n" + "=" * 50)
print("CONTOH 2: Array lebih besar")
print("=" * 50)
random.seed(42)
A2 = random.sample(range(1, 50), 10)
B2 = random.sample(range(1, 50), 10)
k2 = 15

print(f"Array A: {sorted(A2)}")
print(f"Array B: {sorted(B2)}")
print(f"k = {k2}")

all_sums2 = sorted([a+b for a in A2 for b in B2])
print(f"\n{k2} terkecil (brute force): {sorted(all_sums2[:k2])}")

css2 = CartesianSumSelection(A2, B2)
result2 = css2.select(k2)
print(f"{k2} terkecil (CartesianSumSelection): {sorted(result2)}")

print("\n" + "=" * 50)
print("CONTOH 3: LayerOrderedHeap saja")
print("=" * 50)
arr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
print(f"Array asli: {arr}")
loh = LayerOrderedHeap(arr)
print(f"Jumlah layer: {len(loh)}")
for i in range(len(loh)):
    print(f"  Layer {i}: {loh[i]}  | min={loh.min(i)}, max={loh.max(i)}")