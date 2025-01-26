import sys

# 郵便番号の検索プログラム
def find_zip_number(addr):
    count = 0 # ヒット総数を数える

    # CSVファイルを開く
    try:
        # "KEN_ALL_ROME.CSV"というファイルをShift-JISエンコーディングで読み込みモードで開く
        with open("KEN_ALL_ROME.CSV", "rt", encoding="shift-jis") as fp:
            lines = fp.readlines()
    except FileNotFoundError:
        print("CSVファイルが見つかりません。ファイル名を確認してください。")
        sys.exit()

    cleaned_lines = []
    for line in lines:
        # 住所から半角スペースおよび全角スペースと引用符を取り除く
        line = line.replace(' ', '').replace('　', '').replace('"', '')
        cleaned_lines.append(line)

    # 一行ずつ読んで住所の一致を調べる
    results = {}
    for line in cleaned_lines:
        # カンマで区切りリストに変換
        cells = line.split(",")
        
        # 各項目を取得
        zipnumber = cells[0] # 郵便番号
        ken = cells[1]       # 都道府県名
        shi = cells[2]       # 市区
        cho = cells[3]       # 町村
        
        # 都道府県名、市区町村名を結合
        title = ken + shi + cho
        
        # 入力された住所がこの行の住所に含まれるか調べる
        if addr in title:
            results[zipnumber] = title
            count += 1

    # 検索結果を表示
    if not results:
        print("該当する住所は見つかりませんでした。\n注：丁目以降はのぞいて検索してください。")
    else:
        for k in results.keys():
            print(f"{k} : {results[k]}")
        print(str(count) + "件ヒットしました。")

    # ファイルを閉じる
    fp.close()

if __name__ == "__main__":
    # コマンドライン引数を確認
    if len(sys.argv) <= 1:
        print("以下のように入力してください")
        print("python3 find_zip_number.py (住所)")
        sys.exit()
    addr = sys.argv[1].strip()
    find_zip_number(addr)
