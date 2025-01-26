import numpy as np

# クラス1用のサンプル入力データ
teacher_class1 = [[1,3,0,3],[1,4,3,5],[1,6,4,2]]
# クラス2用のサンプル入力データ
teacher_class2 = [[1,1,2,1],[1,3,5,77],[1,4,6,6]]

# 分類用のテストデータ
tests = [[1,2,2,11],[1,5,6,2]]

# 各クラス用の初期重みベクトル
w = [[1,0,0,0],[1,0,0,0]]

# 学習率
p = 1

def judge(w, subject):
    """
    与えられた重みに基づいて、サブジェクトがどのクラスに所属するかを判断する。
    :param w: 各クラスの重みベクトルのリスト
    :param subject: サブジェクトベクトル
    :return: クラス番号（"1"または"2"）を文字列として返す
    """
    g1 = np.array(w[0]).dot(np.array(subject))
    g2 = np.array(w[1]).dot(np.array(subject))
    answer = "1" if max([g1,g2]) == g1 else "2"
    return answer

def perceptron(w, teacher, classNo):
    """
    パーセプトロン学習ルールを使用して、特定のクラスの重みを学習する。
    :param w: 各クラスの重みベクトルのリスト
    :param teacher: 特定のクラスの学習データ
    :param classNo: 学習対象のクラス番号（1または2）
    """
    for i in range(len(teacher)):
        answer = judge(w, teacher[i])
        if (int(answer) != classNo):
            w[classNo-1] += p * np.array(teacher[i])
            w[int(answer)-1] -= p * np.array(teacher[i])

def check(w, teacher, classNo):
    """
    全てのサブジェクトが正しく分類されているかどうかを確認する。
    :param w: 各クラスの重みベクトルのリスト
    :param teacher: 特定のクラスの学習データ
    :param classNo: 確認対象のクラス番号（1または2）
    :return: 全てのサブジェクトが正しく分類されていればTrue、そうでなければFalseを返す
    """
    corrects = 0
    for i in range(len(teacher)):
        answer = judge(w, teacher[i])
        if (int(answer) == classNo):
            corrects += 1
    return corrects == len(teacher)

# 最初にクラス2を学習する
perceptron(w, teacher_class2, 2)
print(w)

# 全てのサブジェクトが両クラスで正しく分類されるまで、反復的に学習する
while(not check(w, teacher_class1, 1) or not check(w, teacher_class2, 2)):
    perceptron(w, teacher_class1, 1)
    perceptron(w, teacher_class2, 2)
    print(w)

# 最終的な重みベクトルを出力する
print("w1 =", w[0], "w2 =", w[1])

# テストデータの分類
print("No.7 belongs to class", judge(w, tests[0]))
print("No.8 belongs to class", judge(w, tests[1]))
