import time
while True :

    time.sleep(5)
    import random
    element = "0123456789azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
    passwd = ""

    for i in range(10):
        passwd = passwd + element[random.randint(0, len(element) - 1)]
    print(passwd)