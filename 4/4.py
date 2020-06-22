from typing import List


class Solution:
    def get_kth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 让 len1 的长度小于 len2，这样就能保证如果有空数组了，一定是len1
        if len1 > len2:
            return self.get_kth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        
        if k == 1:
            return min(nums1[start1], nums2[start2])
        
        i = start1 + min(len1, k//2) - 1
        j = start2 + min(len2, k//2) - 1
        if nums1[i] > nums2[j]:
            return self.get_kth(nums1, start1, end1, nums2, j+1, end2, k-(j-start2+1))
        else:
            return self.get_kth(nums1, i+1, end1, nums2, start2, end2, k-(i-start1+1))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2
        # 将偶数和奇数的情况合并，如果是奇数，会求两次同样的k
        return (self.get_kth(nums1, 0, n-1, nums2, 0, m-1, left) + self.get_kth(nums1, 0, n-1, nums2, 0, m-1, right)) * 0.5


if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
