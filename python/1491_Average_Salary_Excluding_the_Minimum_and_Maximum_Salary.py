class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary) - salary[0] - salary[-1]) / (len(salary) - 2)