import csv

layers = {}

def lohify_project(filepath):
    layers = {}

    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            project = int(row["project"])
            buckets = project // 10

            if buckets not in layers:
                layers[buckets] = []
            layers[buckets].append(project)

    for bucket in layers:
        layers[bucket].sort()

    return layers

x_layers = lohify_project("Student Database.csv")
print(f'Project Grade Layers: {x_layers}')


#===============================================================


def lohify_finals(filepath):
    layers = {}

    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            finals = int(row["final_exam"])
            buckets = finals // 10

            if buckets not in layers:
                layers[buckets] = []
            layers[buckets].append(finals)

    for bucket in layers:
        layers[bucket].sort()

    return layers

y_layers = lohify_finals("Student Database.csv")
print(f'Final Exam Grade Layers: {y_layers}')

#===============================================================
#                     Making The Grids
# The grid is a 10x10 matrix where each cell represents a range of grades (0-9, 10-19, ..., 90-100).
# Each cell will contain the count of students whose project and final exam grades fall within that range
#===============================================================

grid = {}

for x_buckets in x_layers:
    for y_buckets in y_layers:
        min_corner = x_layers[x_buckets][0] + y_layers[y_buckets][0]
        max_corner = x_layers[x_buckets][-1] + y_layers[y_buckets][-1]
        print(f'Grid X : {x_buckets}, Y : {y_buckets}   →   min : {min_corner}, max : {max_corner}')

        grid[(x_buckets, y_buckets)] = {   # ← add this
            "min": min_corner,
            "max": max_corner
        }

print(grid)
