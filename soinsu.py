number = input('number?: ')
print('Number : ' + str(number))
soinsu = []
# print(soinsu)
# ここまでは、普通に入力値を決めて入力値を表示
# 素因数の結果を [a, a, b,....] と表示するためのリストをまずは空で用意
# こういうことしために a = int(number)　と記して数値処理する

a = int(number)


if a == 1:
	print(a)		
	soinsu.append(a)
	
elif a == 0:
	print(a)


# 0, 1は例外的に処理する

else:
	for i in range(2, a):
		while a % i == 0:
			a = a // i
			
#			print(i)
# 2 から a の範囲で　a の剰余を取り、0であるかぎり割り続けるこれがポイント
# 小さい素数から割り続けるので、決して 4 とか 6 などが出てくることはない

			soinsu.append(i)
#			print(soinsu)
# a (素数)　相当をリストに追加


print(soinsu)

# 素因数の結果を [a, a, b,....] と表示


soinsuresult = map(str, soinsu)
result = soinsuresult

# print(list(soinsuresult))

# print(result) 
# とすると　<map object at 0x1089b0ee0>
# map 関数
# https://www.tech-teacher.jp/blog/python-map/
# list1 = [1,2,3,4,5]
# print(list1)
# print(list(map(str, list1))) => ['1', '2', '3', '4', '5']


result = ' x '.join(soinsuresult)
# はじめ list[0]　は　result にある

print(result)


print(str(number) + ' = ' + result)
# 入力数値　＝　a x a x b ...