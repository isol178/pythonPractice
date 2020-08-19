#郵便番号検索
import sys

#コマンドライン引数を確認
if len(sys.argv) <= 1:
    print("以下のように入力してください")
    print("python3 find_zip_number.py (住所)")
    sys.exit()
addr = sys.argv[1].strip()
count = 0 #ヒット総数を数える

#csvファイルを開く
fp = open("KEN_ALL_ROME.CSV", "rt", encoding = "shift-jis")

#一行ずつ読んで住所の一致を調べる
for line in fp:
    line = line.replace(' ','')
    line = line.replace('　','')
    line = line.replace('"', '')
    cells = line.split(",")
    zipnumber = cells[0] #郵便番号
    ken = cells[1] #都道府県名
    shi = cells[2] #市区
    cho = cells[3] #町村
    title = ken + shi + cho
    if title.find(addr) >= 0:
        print(zipnumber+":"+title)
        count += 1
if count == 0: print("該当する住所は見つかりませんでした。\n注：丁目以降はのぞいて検索してください。")
else: print(str(count)+"件ヒットしました。")
fp.close()