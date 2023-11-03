# リストを定義する

# 動物名を格納するリストを定義する
animals = ['panda', 'gorilla', 'dog', 'cat']

print('-----------------------------')

# オブジェクトの型を調べる
print(type(animals))

print('-----------------------------')

# listの中身を出力する
print(animals)

print('-----------------------------')

# len()関数でリストの長さを取得する
list_length = len(animals)
print(list_length)

print('-----------------------------')

# append()関数でリストの後ろに要素を追加する
animals.append('snake')
print(animals)

print('-----------------------------')

# pop()関数でリストから指定の要素を取り出す
animals.pop(1)
print(list_length)
print(animals)

print('-----------------------------')

# insert()関数で指定の要素をリストの先頭に追加する

animals.insert(3, 'dog')
print(animals)

print('-----------------------------')

# count()関数でリスト内の指定の値の数を調べる
print(animals.count('dog'))

# remove()関数でリストから指定した引数と同じ値を削除する
animals.remove('dog')
print(animals)

animals.remove('snake')
print(animals)


# 引数に入れた値を指定の数リストの最後に追加するメソッドを定義してみる
def add_list_double(times, value, array):
    # arrayがlistであるかどうかを最初に判定する必要がある
    if type(array) is not list:
        return
    for i in range(times):
        array.append(value)


# human(人間）を三人文animalのlistの最後尾に入れる
add_value = 'human'
add_list_double(3, add_value, animals)
print(animals)
