import time
from random import randint, choice

times = int(input("题目个数（请输入>0的整数）："))
ordi = int(input("取值范围（请输入>0的整数）："))
num_dui = 0
num_cuo = 0

for i in range(times):
    # 生成算式
    while True:
        fuhao = choice(["+", "-", "*", "/"])
        op1 = randint(0, ordi)
        op2 = randint(0, ordi)
        suan_shi = str(op1)+fuhao+str(op2)

        # 判断除数是否为0和是否为分数
        if op2 == 0 and fuhao == "/":
            continue
        else:
            real_ans = eval(suan_shi) # 除数不为0时生成结果
            if real_ans is not int and '.' in str(real_ans):
                continue
            else:
                break
            
    ans = int(input(suan_shi+"=")) # 输入

    # 判断正误
    if ans == real_ans:
        print("Good job!")
        num_dui += 1
    else:
        print("Sorry!Work hard!")
        print(suan_shi+"="+str(real_ans))
        num_cuo += 1
    print()

print(f"结果：对了{num_dui}个，错了{num_cuo}个")

time.sleep(5)

