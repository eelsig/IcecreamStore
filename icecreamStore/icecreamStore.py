'''
Project : icecream store
Date : 221016
Programmer : Kim Yongoh
'''

def getNewMenuBoard(taste : list, ice : list, price : dict) -> dict:
    # price = {'기본' : 1000, '샌드' : 400, '터키' : 500, '메론' : 200}
    menu = [] 
    for t in taste:
        for i in ice:
            menu.append(' '.join([t, i]))

    menu_price = {}
    for m in menu:
        menu_price[m] = price['기본']
        for k in price:
            if m.count(k) > 0:
                menu_price[m] += price[k]

    return menu_price
def printMenuBoard(board : dict) -> None:
    for i in board:
        print(i, '\t:\t', board[i], sep='')


myBoard = getNewMenuBoard(\
    taste = ['플레인', '사과맛', '포도맛', '메론맛', '복숭아맛'], \
    ice = ['소프트', '하드', '샤베트', '튜브형', '샌드', '터키'],\
    price = {'기본' : 1000, '사과맛' : 100, '포도맛' : 100, '메론맛' : 300, '복숭아맛' : 300, \
        '소프트' : 200, '하드' : 100, '샤베트' : 500, '튜브형' : 200, '샌드' : 400, '터키' : 700})

printMenuBoard(myBoard)