###  釧網本線主要駅のリスト作成
list_senmou_test = [
'網走', '知床斜里', '緑', '川湯温泉', '摩周', '標茶', '釧路' ]

### 区間リストをつくる
seg_list = []
for s in range(len(list_senmou_test)-1):
	seg = list_senmou_test[s:s+2]
	seg_list.append(seg)

## '標茶 - 釧路' とか隣あう二つをまとめたリストに変換
seg_list2 = []
for s in range(len(seg_list)): 
	ss =  ' - '.join(seg_list[s])
	seg_list2.append(ss)
# print(seg_list2)	 

### 列車名入力、区間を表記
train4721d = ['摩周', '釧路']
train4723d = ['川湯温泉', '釧路']
train4725d = ['網走', '釧路']
train3727d = ['網走', '釧路']
train4729d = ['網走', '釧路']
train4731d = ['網走', '釧路']
train4733d = ['網走', '釧路']
train4735d = ['網走', '知床斜里']
train4737d = ['網走', '知床斜里']

trains = [train4721d, train4723d, train4725d, train3727d, train4729d, train4731d, train4733d, train4735d,train4737d]

### 数える本体
default =[]
for i in list_senmou_test:
    default.append(0)
# 駅リストを数値化し、[0...0]を作る。実は使わない。

traincount = []
for j in trains:
	count = [] 
	for k in j:				
		m = list_senmou_test.index(k)
		count.append(m)
	traincount.append(count)	
# print(traincount)
# 起点終点を列車ごと数値化する --> [[0, 6], [1, 4],...]

def2 = []
for i in seg_list2:
    def2.append(0)
# 駅間リスト [0...0]を作る。これを使って数える
 
#traincount再び一個ずつ取り出し、x[0], x[1] 間を 1 として上書きし、
# for 回すことで、全列車を走査し、最終的に総和をとっている
# def2 が最終出力
   
for p in traincount:
	x = p
	list_def2 = def2
	for i in range(x[0], x[1]):
		list_def2[i] = list_def2[i]+1
# print(def2)

### 駅名 vs 本数 zip で表表記
for seg_list2, def2 in zip(seg_list2, def2):
	print(seg_list2, def2)


