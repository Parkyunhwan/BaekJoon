# 1회차 -> 성공 (더 안해도 됨)
# 아마 파이썬의 sort가 안정 정렬이여서 내 코드가 가능하지 않을까 싶다. 불안정이면 할 때마다 순서가 바뀔듯?
# https://github.com/ndb796/python-for-coding-test/blob/master/14/1.py
# 나동빈님의  리버스 적용방법과 람다를 한번에 적용할 수 잇는 것도 참고하자 (이게 훠얼씬 효율적일듯)
# 또한, 문자열을 소팅할때 int형으로 바꿔도 된다.. ㄷㄷ
n = int(input())


info = [input().split() for _ in range(n)]
for i in info:
    i[1:] = map(int, i[1:])

info.sort(key=lambda x: x[0])
info.sort(key=lambda x: x[3], reverse=True)
info.sort(key=lambda x: x[2])
info.sort(key=lambda x: x[1], reverse=True)

for i in range(n):
    print(info[i][0])

############ nbd 코
n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
