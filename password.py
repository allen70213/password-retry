password = 'a123456'
chance = 3
while chance > 0 :
    chance = chance - 1
    answer = input('請輸入密碼: ')
    if answer == password :
        print('登入成功')
        break
    else :
        print('密碼錯誤!')
        if chance > 0:
            print('還有', chance, '次機會')
        else:
            print('你已錯3次密碼，沒機會嘗試了')


