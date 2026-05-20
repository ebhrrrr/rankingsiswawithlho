def median_of_medians_select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(median_of_medians_select(subList, int((len(subList)-1)/2)))
    med = median_of_medians_select(Meds, int((len(Meds)-1)/2))
    L1, L2, L3 = [], [], []
    for i in L:
        if i < med: L1.append(i)
        elif i > med: L3.append(i)
        else: L2.append(i)
    if j < len(L1): return median_of_medians_select(L1, j)
    elif j < len(L2)+len(L1): return L2[0]
    else: return median_of_medians_select(L3, j-len(L1)-len(L2))

def partition(array, left_n):
    n = len(array)
    right_n = n - left_n
    max_value_in_left = median_of_medians_select(array, left_n-1)
    left, right = [], []
    for i in range(n):
        if array[i] < max_value_in_left: left.append(array[i])
        elif array[i] > max_value_in_left: right.append(array[i])
    num_at_threshold_in_left = left_n - len(left)
    left.extend([max_value_in_left]*num_at_threshold_in_left)
    num_at_threshold_in_right = right_n - len(right)
    right.extend([max_value_in_left]*num_at_threshold_in_right)
    return left, right

def layer_order_heapify_alpha_eq_2(array):
    n = len(array)
    if n == 0: return []
    if n == 1: return array
    new_layer_size = 1
    layer_sizes = []
    remaining_n = n
    while remaining_n > 0:
        if remaining_n >= new_layer_size: layer_sizes.append(new_layer_size)
        else: layer_sizes.append(remaining_n)
        remaining_n -= new_layer_size
        new_layer_size *= 2
    result = []
    for i, ls in enumerate(layer_sizes[::-1]):
        small_vals, large_vals = partition(array, len(array)-ls)
        array = small_vals
        result.append(large_vals)
    return result[::-1]

class LayerOrderedHeap:
    def __init__(self, array):
        self._layers = layer_order_heapify_alpha_eq_2(array)
        self._min_in_layers = [min(layer) for layer in self._layers]
        self._max_in_layers = [max(layer) for layer in self._layers]
    def __len__(self): return len(self._layers)
    def __getitem__(self, layer_num): return self._layers[layer_num]
    def min(self, layer_num):
        assert(layer_num < len(self))
        return self._min_in_layers[layer_num]
    def max(self, layer_num):
        assert(layer_num < len(self))
        return self._max_in_layers[layer_num]
    def __str__(self): return str(self._layers)