class Set:
    def __init__(self, nums):
        self.nums = nums

    def get_subsets(self):
        subsets = [[]]
        for i in self.nums:
            subsets += [lst + [i] for lst in subsets]
        return subsets


set = Set([1, 2, 3])
print(set.get_subsets())
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
