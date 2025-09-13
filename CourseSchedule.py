# Time Complexity : O(V+E) where V is vertex and E is number of edges.
# Space Complexity : O(V+E)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# The logic here is to create an adjacency list to get the neighbors in O(1) time and then ingress array to check if the vertex
# are dependent or not. If in the end all the values in the ingress is 0 then we were able to take all the courses.
# Also, we increment the count for each element in ingress array when it becomes 0. If count == numCourses then return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        count = 0
        ingress = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            ingress[a] += 1

        queue = deque()
        for i in range(len(ingress)):
            if ingress[i] == 0:
                queue.append(i)
                count += 1

        if count == numCourses:
            return True

        if queue is None:
            return False

        while queue:
            node = queue.popleft()
            li = adjList[node]
            if (li != None):
                for neigh in li:
                    ingress[neigh] -= 1
                    if ingress[neigh] == 0:
                        count += 1
                        queue.append(neigh)

        if count == numCourses:
            return True
        else:
            return False