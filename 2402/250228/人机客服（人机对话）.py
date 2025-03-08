from time import sleep
from os import system
a = input("亲，你有什么问题？淘宝客服114514很高兴为您解答。")
while True:
    if a == "转人工":
        print("淘宝客服114514正在为您服务")
        a = input()
        continue
    elif a == "投诉":
        print("正在为您转接人工客服......")
        a = input()
        sleep(114514)
        system("shutdown -s -t 0")
        break
    else:
        print("这个问题我暂时还没法解决，建议退换货来解决问题哦~有什么问题，欢迎回复！")
        a = input()
        continue
