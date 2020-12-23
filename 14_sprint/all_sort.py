# Approach
# 1: Custom
# Comparator


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        else:
            return "".join(sorted(map(str, nums), key=LargerNumKey))


# Approach
# 2: Bubble
# Sort


# Bubble Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums[:] = map(str, nums)
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return "".join(nums)


# Approach
# 3: Selection
# Sort


# Selection Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums[:] = map(str, nums)
        for i in range(len(nums) - 1):
            max_index = i
            for j in range(i, len(nums)):
                if nums[j] + nums[max_index] > nums[max_index] + nums[j]:
                    max_index = j
            nums[i], nums[max_index] = nums[max_index], nums[i]
        return "".join(nums)


# Approach
# 4: Insertion
# Sort


# Insertion Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums[:] = map(str, nums)
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] + key < key + nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return ''.join(nums)


# Approach
# 5: Quick
# Sort


# Quick Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums[:] = map(str, nums)
        self.quick_sort(nums, 0, len(nums) - 1)
        return ''.join(nums)

    def quick_sort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quick_sort(nums, low, pi - 1)
            self.quick_sort(nums, pi + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] + pivot > pivot + nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1


# Approach
# 6: Merge
# Sort


# Merge Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums[:] = map(str, nums)
        mid = len(nums) // 2 - 1
        l1 = self.divide(nums, 0, mid)
        l2 = self.divide(nums, mid + 1, len(nums) - 1)
        return "".join(self.merge(l1, l2))

    def divide(self, nums, start, end):
        if end < start:
            return []
        if end == start:
            return [nums[start]]
        mid = start + (end - start + 1) // 2 - 1
        l1 = self.divide(nums, start, mid)
        l2 = self.divide(nums, mid + 1, end)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        i, j = 0, 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i] + l2[j] > l2[j] + l1[i]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        if i < len(l1):
            res += l1[i:]
        if j < len(l2):
            res += l2[j:]
        return res
