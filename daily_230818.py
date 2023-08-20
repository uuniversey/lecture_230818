

# 1226. 미로1

# import sys
# sys.stdin = open('input_1226.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     result = 0
#     queue = []
#     queue.append([1,1])         # q에 리스트로 된 인덱스 값을 넣어준다.
#     visited = [[0] * 16 for _ in range(16)]     # 방문 이력 검사용
#     visited[1][1] = 1           # 스타트 위치 방문 표시
#
#     while len(queue) != 0:      # q가 빌 때까지 진행할 것이므로 길이 막혀 있지 않다면 계속 진행할 것이다.
#         site = queue.pop(0)
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             if maze[site[0]+di][site[1]+dj] == 0 and visited[site[0]+di][site[1]+dj] == 0:
#                 queue.append([site[0]+di, site[1]+dj])
#                 visited[site[0]+di][site[1]+dj] = 1
#         # q에서 꺼낸 인덱스를 중심으로 사방을 확인해서 0인 경우 즉 길인 경우를 q에 넣고 방문 표시를 한다.
#
#             elif maze[site[0]+di][site[1]+dj] == 3:
#                 result = 1
#                 queue.clear()
#                 break
#         # 만약에 사방에 3이 존재한다면 길이 이어진다는 소리이므로 result를 1로 바꾸고 큐를 비워서 while문 탈출
#
#     print(f'#{tc} {result}')




# 1227. 미로2

# import sys
# sys.stdin = open('input_1227.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(100)]
#     result = 0
#     queue = []
#     queue.append([1,1])         # q에 리스트로 된 인덱스 값을 넣어준다.
#     visited = [[0] * 100 for _ in range(100)]     # 방문 이력 검사용
#     visited[1][1] = 1           # 스타트 위치 방문 표시
#
#     while len(queue) != 0:      # q가 빌 때까지 진행할 것이므로 길이 막혀 있지 않다면 계속 진행할 것이다.
#         site = queue.pop(0)
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             if maze[site[0]+di][site[1]+dj] == 0 and visited[site[0]+di][site[1]+dj] == 0:
#                 queue.append([site[0]+di, site[1]+dj])
#                 visited[site[0]+di][site[1]+dj] = 1
#         # q에서 꺼낸 인덱스를 중심으로 사방을 확인해서 0인 경우 즉 길인 경우를 q에 넣고 방문 표시를 한다.
#
#             elif maze[site[0]+di][site[1]+dj] == 3:
#                 result = 1
#                 queue.clear()
#                 break
#         # 만약에 사방에 3이 존재한다면 길이 이어진다는 소리이므로 result를 1로 바꾸고 큐를 비워서 while문 탈출
#
#     print(f'#{tc} {result}')


# 1238. Contact

# import sys
# sys.stdin = open('input_1238.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     data, start = map(int, input().split())
#     arr = list(map(int, input().split()))
#     emer_call = [[] for _ in range(101)]
#     visited = [0] * 101
#     visited[start] = 1
#     queue = []
#     queue.append(start)
#     max_v = 0
#     max_num = 0
#
#     for i in range(data//2):
#         v1, v2 = arr[2*i], arr[2*i+1]
#         emer_call[v1].append(v2)        # 단방향 이므로
#
#     while len(queue) != 0:
#         site = queue.pop(0)
#         for j in emer_call[site]:
#             if visited[j] == 0:
#                 queue.append(j)
#                 visited[j] = visited[site] + 1
#
#     for k in range(len(visited)):       # 가장 마지막으로 연락 받은 곳이 몇번째 인지를 찾음
#         if max_v < visited[k]:
#             max_v = visited[k]
#
#     for l in range(len(visited)):       # 그 중에 가장 숫자가 큰 사람 찾아서 출력
#         if visited[l] == max_v:
#             if max_num < l:
#                 max_num = l
#
#     print(f'#{tc} {max_num}')


# 5102. 노드의 거리

# import sys
# sys.stdin = open('input_5102.txt', 'r')

# T = int(input())
#
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     arr = [[] for _ in range(V+1)]
#     for _ in range(E):
#         v1, v2 = map(int, input().split())
#         arr[v1].append(v2)
#         arr[v2].append(v1)
#     S, G = map(int, input().split())
#     visited = [0] * (V+1)
#     visited[S] = 1
#     queue = []
#     queue.append(S)
#
#     while len(queue) != 0:
#         site = queue.pop(0)
#         if site == G:
#             break
#         for i in arr[site]:
#             if visited[i] == 0:
#                 visited[i] = visited[site] + 1
#                 queue.append(i)
#
#     if site != G:
#         print(f'#{tc}', 0)
#     else:
#         print(f'#{tc} {visited[site]-1}')


# 5105. 미로의 거리

# import sys
# sys.stdin = open('input_5105.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list((input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     queue = []
#     site_row = 0
#     site_col = 0
#     complete = False
#
#     for row in range(N):
#         for col in range(N):
#             if maze[row][col] == '2':           # 시작점 찾기
#                 visited[row][col] = 1
#                 queue.append([row, col])
#
#     while len(queue) != 0:                      # q가 빌 때까지
#         site = queue.pop(0)
#         site_row = site[0]
#         site_col = site[1]
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             if 0 <= site_row + di < N and 0 <= site_col + dj < N:
#                 if maze[site_row+di][site_col+dj] == '0' and visited[site_row+di][site_col+dj] == 0:
#                     queue.append([site_row+di, site_col+dj])
#                     visited[site_row+di][site_col+dj] = visited[site_row][site_col] + 1
#
#                 elif maze[site_row+di][site_col+dj] == '3':
#                     visited[site_row+di][site_col+dj] = visited[site_row][site_col] + 1
#                     queue.clear()               # q를 비워서 for문 탈출
#                     complete = True             # 3까지 가는 길이 있다는 것 확인
#                     break
#
#     if complete == True:        # 3까지 가는 길 있다는거 확인한 경우
#         print(f'#{tc} {visited[site_row+di][site_col+dj] - 2}')     # visited를 1부터 시작했고 마지막에도 1을 더해줬으므로 2를 뺀다.
#
#     else:                       # while문 다 돌고도 길 확인 못한 경우
#         print(f'#{tc} {0}')



# 18459. BFS 연습

# import sys
# sys.stdin = open('input_18459.txt', 'r')
#
# T = 1
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     arr = list(map(int, input().split()))
#     my_list = [[] for _ in range(V+1)]
#     visited = [0] * (V+1)
#     queue = []
#     queue.append(1)
#     visited[1] = 1
#     result = []
#     for i in range(E):
#         v1, v2 = arr[2*i], arr[2*i + 1]
#         my_list[v1].append(v2)
#         my_list[v2].append(v1)
#
#     while len(queue) != 0:
#         node = queue.pop(0)
#         result.append(node)
#         for j in my_list[node]:
#             if visited[j] == 0:
#                 visited[j] = visited[node] + 1
#                 queue.append(j)
#
#     print(f'#{tc}', *result)