class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        matrix = [[0]*numCourses for _ in range(numCourses)]
        requirements = [0]*numCourses

        for course, pre in prerequisites:
            if matrix[pre][course] == 0:
                requirements[course] += 1
            matrix[pre][course] = 1

        stack = [course for course in range(numCourses) if requirements[course]==0]

        counter = 0
        while stack:
            course = stack.pop(0)
            counter += 1

            for i in range(numCourses):
                if matrix[course][i] != 0:
                    requirements[i] -= 1
                    if requirements[i] == 0:
                        stack.append(i)
        
        return counter == numCourses