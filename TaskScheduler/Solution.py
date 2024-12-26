from collections import defaultdict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        waits = defaultdict(set)
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1
        
        for task in counts:
            waits[0].add(task)
        
        intervals = 0
        while len(tasks) > 0:
            scheduledTask = ""
            # find the task with the highest count from waits[0]
            frequency = 0
            for task in waits[0]:
                if counts[task] > 0 and max(counts[task], frequency) > frequency:
                    scheduledTask = task
                    frequency = counts[task]
            # schedule the task with the highest count & wait of 0
            if scheduledTask != "":
                tasks.pop()
                counts[scheduledTask] -= 1
                waits[0].remove(scheduledTask)
            
            for i in range(1, n+1):
                waits[i-1].update(waits[i])
                waits[i].clear()
            
            if scheduledTask != "":
                waits[n].add(scheduledTask)

            intervals += 1
        
        return intervals

sol = Solution()
tasks = ["A","A","A","B","B","B"]
print(sol.leastInterval(tasks, 3))

tasks = ["A","B","A"]
print(sol.leastInterval(tasks, 2))