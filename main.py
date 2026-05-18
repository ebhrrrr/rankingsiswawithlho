import pandas as pd
import heapq

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("Student Database.csv")

# ==========================================
# HITUNG TOTAL
# ==========================================

df["Total"] = df["Nilai_Ujian"] + df["Nilai_Project"]

# ==========================================
# SORT DESCENDING (MAX HEAP STYLE)
# ==========================================

df_max = df.sort_values(by="Total", ascending=False).reset_index(drop=True)

# ==========================================
# BUILD LOH LAYERS (1,2,4,8,...)
# ==========================================

layers = []

layer_size = 1
index = 0

while index < len(df_max):

    layer = df_max.iloc[index:index + layer_size]

    if len(layer) == 0:
        break

    layers.append(layer)

    index += layer_size
    layer_size *= 2

# ==========================================
# DISPLAY LOH LAYERS
# ==========================================

print("\n===================================")
print("LAYER ORDERED HEAP")
print("===================================")

for i, layer in enumerate(layers):

    max_val = layer["Total"].max()
    min_val = layer["Total"].min()

    print(f"\nLayer {i+1}")
    print(f"Jumlah Data : {len(layer)}")
    print(f"MAX : {max_val}")
    print(f"MIN : {min_val}")

    print(layer[["Nama", "Total"]].to_string(index=False))

# ==========================================
# MAX HEAP
# ==========================================

print("\n===================================")
print("MAX HEAP")
print("===================================")

max_heap = []

for _, row in df.iterrows():

     heapq.heappush(max_heap, (-row["Total"], row["Nama"]))
 
# Pop satu per satu → hasil terurut descending
sorted_desc = []
while max_heap:
    neg_total, nama = heapq.heappop(max_heap)
    sorted_desc.append((nama, -neg_total))
 
print(f"\n{'No':<5} {'Nama':<15} {'Total'}")
print("-" * 30)
for i, (nama, total) in enumerate(sorted_desc, 1):
    print(f"{i:<5} {nama:<15} {total}")

# ==========================================
# TOP-K ATAS
# ==========================================

k = 5

k = 5
 
print(f"\nTOP {k} SISWA TERBAIK\n")
for i, (nama, total) in enumerate(sorted_desc[:k], 1):
    print(f"{i}. {nama} - {total}")

# ==========================================
# MIN HEAP
# ==========================================

print("\n===================================")
print("MIN HEAP")
print("===================================")

min_heap = []
for _, row in df.iterrows():
    heapq.heappush(min_heap, (row["Total"], row["Nama"]))
 
sorted_asc = []
while min_heap:
    total, nama = heapq.heappop(min_heap)
    sorted_asc.append((nama, total))
 
print(f"\n{'No':<5} {'Nama':<15} {'Total'}")
print("-" * 30)
for i, (nama, total) in enumerate(sorted_asc, 1):
    print(f"{i:<5} {nama:<15} {total}")

# ==========================================
# TOP-K BAWAH
# ==========================================

print(f"\nBOTTOM {k} SISWA\n")
for i, (nama, total) in enumerate(sorted_asc[:k], 1):
    print(f"{i}. {nama} - {total}")

# ==========================================
# PRUNING SIMULATION
# ==========================================

print("\n===================================")
print("PRUNING SIMULATION")
print("===================================")

top_students = sorted_desc[:k]
threshold = min([x[1] for x in top_students])
 
print(f"\nCurrent Threshold TOP-{k} = {threshold}")
 
for i, layer in enumerate(layers):
 
    layer_max = layer["Total"].max()
 
    if layer_max < threshold:
        print(f"\nLayer {i+1} PRUNED")
        print(f"Reason : MAX {layer_max} < Threshold {threshold}")
    else:
        print(f"\nLayer {i+1} ACTIVE")
        print(f"Reason : MAX {layer_max} >= Threshold {threshold}")

# ==========================================
# SIMPLE TREE VISUALIZATION
# ==========================================

print("\n===================================")
print("LAYER VISUALIZATION")
print("===================================")

for i, layer in enumerate(layers):

    totals = list(layer["Total"])

    spacing = " " * (30 - (i * 4))

    print(f"\n{spacing}Layer {i+1}")

    print(f"{spacing}MAX={max(totals)}")
    print(f"{spacing}MIN={min(totals)}")

    row_visual = ""

    for val in totals:
        row_visual += f"[{val}] "

    print(spacing + row_visual)
