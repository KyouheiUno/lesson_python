# 辞書型
# 辞書型はキーと値で定義しリストとことなり{}で定義する

# 辞書型を定義
my_status_dict = {
    'first_name': 'kyohei',
    'last_name': 'uno',
    'weight': 70,
    'height': 175,
    'age': 30,
    'blood_type': 'b'
}

# 型を出力
print(type(my_status_dict))

# 値を出力
print(my_status_dict)

# 辞書型をfor文を使ってループ処理をする。keys, valuesのどちらのメソッドも使用しない場合はkeyを取得できる
for hoge in my_status_dict:
    print(hoge)

print('-----------------------------')
# 辞書型をfor文を使ってvalueの値を取得するループ処理をする。
for fuga in my_status_dict.values():
    print(fuga)
