class Set:
    def __init__(self, nums):
        self.nums = nums

    def get_subsets(self):
        subsets = [[]]
        tmp_subsets = [[]]
        for num in self.nums:
            for subset in tmp_subsets:
                subsets += [subset + [num]]
            tmp_subsets = list(subsets)

        return subsets

    def get_subsets_v2(self):
        subsets = [[]]
        for num in self.nums:
            subsets += [subset + [num] for subset in subsets]
        return subsets


set = Set(['a', 'b', 'c'])
print(set.get_subsets())
print(set.get_subsets_v2())
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
