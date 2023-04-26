import sys
import heapq

def project_selection(c, k):
    available_projects = [(project[0], project[1] - project[0]) for project in cr]
    available_projects.sort(key = lambda x: x[0])
    available_projects.append((float('inf'),float('inf')))
    selected_projects = []
    
    for n in range(k):
        while available_projects[0][0] <= c:
            cost, profit = heapq.heappop(available_projects)
            heapq.heappush(selected_projects, -profit)
            
        if not selected_projects:
            return 'impossible'
        
        max_profit = -heapq.heappop(selected_projects)
        
        c += max_profit
    
    return c
