class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees=[0]*numCourses

        for post, pre in prerequisites:
            graph[pre].append(post)
            indegrees[post]+=1
        
        # now sort calculate the indegrees for each node, add all nodes with 0 to queue, decrement each neighbors indegrees, add to queue if anything is 0. pop from queue and add to list
        q = deque(i for i in range(numCourses) if indegrees[i] == 0)
        final=[]

        while q:
            to_add = q.popleft()
            final.append(to_add)
            m = len(graph[to_add])
            for nxt in graph[to_add]:
                indegrees[nxt]-=1
                if indegrees[nxt]==0:
                    q.append(nxt)

        return final if len(final)==numCourses else []

        