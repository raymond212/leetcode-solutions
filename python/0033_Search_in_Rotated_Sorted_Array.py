class Solution1:
    def search(self, a: List[int], target: int) -> int:
        if not a:
            return -1
        
        start, end = 0, len(a) - 1
        while start <= end:
            mid = (start + end) // 2
            if a[mid] == target:
                return mid
            
            if a[mid] >= a[start]:
                if a[start] <= target <= a[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if a[mid] <= target <= a[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1

# failure proof template solution
class Solution2:
    def search(self, a: List[int], target: int) -> int:
        if not a:
            return -1
        
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] > a[start]:
                if a[start] <= target <= a[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if a[mid] <= target <= a[end]:
                    start = mid
                else:
                    end = mid
        
        if a[start] == target:
            return start
        if a[end] == target:
            return end
        return -1