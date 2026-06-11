def square_list(numbers):
    squares = []
    for num in numbers:squares.append(num * num)
    return squares
#リストの作り方
d=[]
d=square_list([2,2,2,2,2,2,2,2])
print(d)
#square_list = [num * num for num in numbers]

"""
import numpy as np

# 係数行列と定数ベクトルの定義
A = np.array([[1, -3, 2], [3, -5, 7], [-2, 7, -6]])
B = np.array([-1, 6, 2])

# 係数行列の逆行列を計算
A_inv = np.linalg.inv(A)

# 方程式の解を計算
solution = np.dot(A_inv, B)

# 解を表示
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])
"""
"""
#a=(q,"qqq",1)←中身を変えたくない時のリスト
q=2+3j
print(a)
"""
# 集合の作成
my_set = {1, 2, 3, 4, 5}

# 集合の要素を追加
my_set.add(6)
print("要素6を追加した後の集合:", my_set)

# 既存の要素を削除
my_set.remove(1)
print("要素3を削除した後の集合:", my_set)

# 要素の有無を確認
print("要素2は集合に含まれていますか？", 2 in my_set)
print("要素7は集合に含まれていますか？", 7 in my_set)

# 集合の長さを取得
print("集合の長さ:", len(my_set))

# 集合の要素をループで処理
print("集合の要素:")
for item in my_set:
    print(item)

# 2つの集合の和、積、差を計算
other_set = {4, 5, 6, 7}
print("集合の和:", my_set.union(other_set))
print("集合の積:", my_set.intersection(other_set))
print("集合の差:", my_set.difference(other_set))
e=[1,2,3,4,5,6,7,8,9,10]
#マイナスが右・:が向き・数値二つで間
print(e[:3])#左から3番目から左
print(e[2:])#左から2番目から右
print(e[-2:])#右から2番目から右
print(e[1:3])#左から1番目から3番目未満の番号まで

def tt(y):#条件式の関数
    if y==1:return True
    if y==0:return False
def t():
    if tt(1):#作った条件式
       print("aa")
t()

a=[0,0,0]
print(len(a))#リストの長さ表示
b="aaaaa"
print(len(b))#文の長さ表示
ii=[None]*10#部屋を10個作る
ii[0]=a
ii[1]=b
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.append(100)#リストの中身加える
ii[2]=my_list
print(my_list)
my_list.insert(2,999)#番号（部屋）を決めて中身加える
print(my_list)
ii[3]=my_list
sorted_list = sorted(my_list)#中身を小さい順に並び替える
print(sorted_list)
ii[4]=my_list
sorted_list = sorted(my_list, reverse=True)#中身を大きい順に並び替える
print(sorted_list)
ii[5]=my_list
oo=[[[10,10],[20,20]],[[30,10],[40,20]]]
ii[0][1]=oo
print("\n\n"+str(ii[0][1][0]))
print(ii)
