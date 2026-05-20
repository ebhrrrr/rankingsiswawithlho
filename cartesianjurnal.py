from LayerOrderedHeap import *
import heapq

class CartesianSumSelection:
    def _min_tuple(self,i,j):
        return (self._loh_a.min(i) + self._loh_b.min(j), (i,j), False)
    def _max_tuple(self,i,j):
        return (self._loh_a.max(i) + self._loh_b.max(j), (i,j), True)
    def _in_bounds(self,i,j):
        return i < len(self._loh_a) and j < len(self._loh_b)
    def _insert_min_if_in_bounds(self,i,j):
        if not self._in_bounds(i,j): return
        if (i,j,False) not in self._hull_set:
            heapq.heappush(self._hull_heap, self._min_tuple(i,j))
            self._hull_set.add((i,j,False))
    def _insert_max_if_in_bounds(self,i,j):
        if not self._in_bounds(i,j): return
        if (i,j,True) not in self._hull_set:
            heapq.heappush(self._hull_heap, self._max_tuple(i,j))
            self._hull_set.add((i,j,True))
    def __init__(self, array_a, array_b):
        self._loh_a = LayerOrderedHeap(array_a)
        self._loh_b = LayerOrderedHeap(array_b)
        self._hull_heap = [self._min_tuple(0,0)]
        self._hull_set = {(0,0,False)}
        self._num_elements_popped = 0
        self._layer_products_considered = []
        self._full_cartesian_product_size = len(array_a) * len(array_b)
    def _pop_next_layer_product(self):
        result = heapq.heappop(self._hull_heap)
        val, (i,j), is_max = result
        self._hull_set.remove((i,j,is_max))
        if not is_max:
            self._insert_min_if_in_bounds(i+1,j)
            self._insert_min_if_in_bounds(i,j+1)
            self._insert_max_if_in_bounds(i,j)
        else:
            self._num_elements_popped += len(self._loh_a[i]) * len(self._loh_b[j])
            self._layer_products_considered.append((i,j))
        return result
    def select(self, k):
        assert(k <= self._full_cartesian_product_size)
        while self._num_elements_popped < k:
            self._pop_next_layer_product()
        for val, (i,j), is_max in self._hull_heap:
            if is_max:
                self._num_elements_popped += len(self._loh_a[i]) * len(self._loh_b[j])
                self._layer_products_considered.append((i,j))
        candidates = [val_a+val_b for i,j in self._layer_products_considered
                      for val_a in self._loh_a[i] for val_b in self._loh_b[j]]
        print('Ratio of total popped candidates to k: {}'.format(len(candidates)/k))
        k_small_vals, large_vals = partition(candidates, k)
        return k_small_vals