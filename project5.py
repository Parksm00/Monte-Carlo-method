import random
import matplotlib.pyplot as plt
import numpy as np

#함수
def func(x):
    return x*x + np.sin(np.pi*(2*x))
    #return x*x

cnt = 0

#값의 범위
x_min = 0
x_max = 1
y_min = -1
y_max = 1.5


#랜덤 샘플링하기
x_list = []
y_list = []
color_list = []
N = 10000 #샘플링 횟수


for i in range(N):
    #랜덤 샘플링(x,y) 생성
    x = random.uniform(x_min,x_max)
    y = random.uniform(y_min,y_max)

    x_list.append(x)
    y_list.append(y)

    if y<=func(x):
        color_list.append('dodgerblue')
        cnt += 1
    else : 
        color_list.append('red')

    
#그래프 그리기
px = np.linspace(x_min, x_max, 1000)
py = func(px)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title("몬테카를로 기법을 이용한 면적계산")

plt.plot(px, py, color = 'black')
plt.scatter(x_list, y_list, color = color_list, s= 3)
plt.grid()
plt.show()

print(cnt/N * 2.5)