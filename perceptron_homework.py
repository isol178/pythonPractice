import numpy as np

teacher_class1 = [[1,3,0,3],[1,4,3,5],[1,6,4,2]]
teacher_class2 = [[1,1,2,1],[1,3,5,77],[1,4,6,6]]
tests = [[1,2,2,11],[1,5,6,2]]
w = [[1,0,0,0],[1,0,0,0]]
p = 1

def judge(w, subject):
    g1 = np.array(w[0]).dot(np.array(subject))
    g2 = np.array(w[1]).dot(np.array(subject))
    answer ="1" if max([g1,g2]) == g1 else "2"
    return answer

def perceptron(w, teacher, classNo):
    for i in range(3):
        answer = judge(w, teacher[i])
        if (int(answer) != classNo):
            w[classNo-1] += p*np.array(teacher[i])
            w[int(answer)-1] -= p*np.array(teacher[i])

def check(w, teacher, classNo):
    corrects = 0
    for i in range(3):
        answer = judge(w, teacher[i])
        if (int(answer) == classNo):
            corrects += 1
    if (corrects == 3):
        return True
    else:
        return False

perceptron(w, teacher_class2, 2)
print(w)
while(not check(w, teacher_class1, 1) or not check(w, teacher_class2, 2)):
    perceptron(w, teacher_class1, 1)
    perceptron(w, teacher_class2, 2)
    print(w)

print("w1 = "+str(w[0])+" w2 = "+str(w[1]))
print("No.7 belongs to class"+judge(w, tests[0]))
print("No.8 belongs to class"+judge(w, tests[1]))
