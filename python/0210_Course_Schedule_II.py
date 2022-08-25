class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * num_courses
        edges = {i : [] for i in range(num_courses)} # course: [list of next courses]

        for course_1, course_2 in prerequisites:
            in_degree[course_2] += 1
            edges[course_1].append(course_2)
        
        queue = collections.deque()
        remain = num_courses
        order = []

        for course in range(num_courses):
            if in_degree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for next_course in edges[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        if len(order) == num_courses:
            return order[::-1]
        
        return []