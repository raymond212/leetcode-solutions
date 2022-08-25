class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * num_courses
        edges = {i : [] for i in range(num_courses)} # course: [list of next courses]

        for course_1, course_2 in prerequisites:
            in_degree[course_2] += 1
            edges[course_1].append(course_2)

        queue = collections.deque()
        remain = num_courses

        for course in range(num_courses):
            if in_degree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            remain -= 1
            for next_course in edges[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return remain == 0