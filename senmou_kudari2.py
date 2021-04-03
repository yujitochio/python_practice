### 全区間リストから主要駅リストを作成する

###  釧網本線主要駅リスト(初期値)
list_senmou_test = []

###  釧網本線主要駅リスト
list_senmou_all = [
'網走', '桂台', '鱒浦', '藻琴', '北浜', '浜小清水', '止別', 
'知床斜里', '中斜里', '清里町', '札弦', '緑',
'川湯温泉', '美留和', '摩周', '磯分内', 
'標茶', '茅沼', '塘路', '細岡', '遠矢', '東釧路', '釧路' ]

### 列車名入力
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

#print(list_senmou_all)
#print(trains[1])

#default = []
#default.extend(trains[1])
#default.extend(trains[7])
#print(len(trains))

defaultlist = []
for i in range(len(trains)):
	defaultlist.extend(trains[i])

#list_senmou_test = []
#for i in trains:
#	default = []
#	default.extend(trains[i])
# print(default)
# print(defaultlist)

for i in range(len(list_senmou_all)):
#	print(name[i])
	if list_senmou_all[i] in defaultlist:
		list_senmou_test.append(list_senmou_all[i])
	
print(list_senmou_test)	

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


