'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# BFS - 인접 리스트

def bfs(s, V):  # 시작 정점 s, 마지막 정점 V
    visited = [0] * (V+1)   # visited 생성
    q = []              # 큐 생성
    q.append(s)         # 시작점 인큐
    visited[s] = 1      # 시작점 방문 표시
    while q:            # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # 디큐
        print(t)        # 방문한 정점해서 할 일
        for w in adj_l[t]:      # 인접한 정점 중 인큐되지 않은 정점이 있으면
            if visited[w] == 0:
                q.append(w)     # 인큐 하고 인큐되었음을 visited에 표시
                visited[w] = visited[t] + 1


V, E = map(int, input().split())    # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 ------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
# 여기까지 인접리스트 ----------------

bfs(1, 7)