#coding:utf-8
from PIL import Image, ImageDraw, ImageFont
import random

OFF, ON = 0, 1

def dec2bin(n):
    """10進数を2進数の01リストに変換
    下位ビットから順番に並べる"""
    bit_list = []
    for i in range(6):
        bit_list.append(int(n % 2))
        n /= 2
    print(bit_list)
    return bit_list

def ca(width, height, rulenum):
    """1次元セルオートマトンの図を描画"""
    results = []

    # 初期状態
    first_row = [0] * width
    for i in range(300):
        if(random.random() < 0.5):
            first_row[i] = ON
    results.append(first_row)

    # ルールの番号から次の状態のビット列を得る
    rule = dec2bin(rulenum)

    for i in range(height - 1):
        old_row = results[-1]
        new_row = []
        for j in range(width):
            # widthの剰余を取るのは、端同士がつながっているため
            n = old_row[(j-2)%width] + old_row[(j-1)%width] + old_row[j] + old_row[(j+1)%width] + old_row[(j+2)%width]
            new_row.append(rule[int(n)])
        results.append(new_row)
    return results

def render(results, width, height, filename="SUMrule42.png"):
    """セルオートマトンを描画"""
    img = Image.new("RGB", (width, height), (255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if results[y][x] == ON:
                draw.point((x, y), (0, 0, 0))
    img.save(filename, "PNG")

if __name__ == "__main__":
    width, height = 300, 150
    rulenum = 42
    results = ca(width, height, rulenum)
    render(results, width, height)