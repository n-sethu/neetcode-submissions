class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        if prerequisites is None:
            return [i for i in range(numCourses)]
        
        n = len(prerequisites)
        indegrees=[0]*numCourses

        for i in range(n):
            pre=prerequisites[i][1]
            post =prerequisites[i][0]
            graph[pre].append(post)
            indegrees[post]+=1
        
        # now sort
        # calculate the indegrees for each node, add all nodes with 0 to queue, decrement each neighbors indegrees, add to queue if anything is 0. pop from queue and add to list
        q = deque()
        for i in range(numCourses):
            if(indegrees[i]==0):
                q.append(i)
        final=[]
        while q:
            to_add = q.pop()
            # print(to_add)
            m = len(graph[to_add])
            for j in range(m):
                indegrees[graph[to_add][j]]-=1
                if indegrees[graph[to_add][j]]==0:
                    q.append(graph[to_add][j])
            final.append(to_add)
        # print(final,indegrees,graph,q)
        return final if len(final)==numCourses else []

        