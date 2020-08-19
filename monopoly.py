#モノポリーで各マスに止まる確率をシミュレーションで計算する
import random
import time
number_of_players = 3 #プレーヤーの数
Players = [0]*number_of_players #プレーヤー位置の変数
Probability = [0]*40 #確率計算用
game_length = 20 #ダイスを振る回数

#ダイスによるゲーム進行
def dice():
    number = 0
    number += random.randint(1,6)
    time.sleep(0.01)
    number += random.randint(1,6)
    return number

#チャンス判定
def isChance(location):
    if location == 7 or location == 22 or location == 36:
        return True

#チャンス処理
def doChance(location):
    card = 0
    card = random.randint(1,16)
    if card == 1: #ボードウォークに進む
        return 39
    elif card == 2: #GOに進む
        return 0
    elif card == 3: #刑務所にいく
        return 10
    elif card == 4: #リーディング鉄道に進む
        return 5
    elif card == 5: #イリノイ通りに進む
        return 24
    elif card == 6: #セントチャールズプレースに進む
        return 11
    elif card == 7: #次の水道会社か電力会社に進む
        if location == 22:
            return 28
        else:
            return 12
    elif card == 8 or card == 9: #次の鉄道まで進む
        if location == 7:
            return 15
        elif location == 22:
            return 25
        elif location == 36:
            return 5
    else:
        return location

print("ゲーム開始")
increase_counter = 0
for i in range(game_length):
    for j in range(number_of_players):
        Dice = dice()
        #print(Dice)
        Players[j] += Dice
        if Players[j] > 39:
            Players[j] -= 40
        Probability[Players[j]] += 1
        if Players[j] == 30:
            Players[j] = 1
            Probability[Players[j]] += 1
            increase_counter += 1
        if isChance(Players[j]):
            Players[j] = doChance(Players[j])
            if not(Players[j] == 7 or Players[j] == 22 or Players[j] == 36):
                Probability[Players[j]] += 1
                increase_counter += 1

print("結果発表")
a = 0
for i in Probability:
    i = i/(game_length*number_of_players + increase_counter)*100
    print(str(a)+"番のマス："+str(i)+"％")
    a += 1
