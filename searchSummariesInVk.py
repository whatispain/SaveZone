#7 дней
from datetime import datetime
import vk_api
from collections import defaultdict


def CastUnixDateTimeToClassicDateTime(timeStamp): #На вход подать дату и время unix формата "1654626695"
    return datetime.utcfromtimestamp(int(timeStamp)).strftime('%Y-%m-%d %H:%M:%S') #Возвращяет "2022-06-07 18:31:35"

def ExtrudeAddress(textContainingStreets: str,streetList: list): #Метод выделяет из строки названия улиц.
    theTrigger: bool = False #Триггер, указывающий что следующий элемент - улица.
    textWords = textContainingStreets.split(" ")
    for word in textWords:
        if (theTrigger == True):#Если текущий элемент - слово, запомнить.
            streetList.append(word) if word.isalpha() == True else streetList.append(word[0:len(word)-1])
            #streetList.append(word)
            #print("Если слово", word)
            theTrigger = False #Сбросить триггер
            continue
        if (word.find("ул.") != -1):#Если следующий элемент - слово, установить триггер.
            theTrigger = True
            continue

def VkTakeSummariesInPublic():
    vk_session = vk_api.VkApi('NumPhone', 'YouPassword')
    vk_session.auth()
    vk = vk_session.get_api()
    rawListItemsText=[]
    wallPost = vk.wall.search(owner_id='-57424472', query="- ул.", count=10)  # Вернет Словарь в списке в словаре
    wallPostItems = wallPost["items"]
    for items in wallPostItems:
        rawListItemsText.append(items["text"])
    return rawListItemsText

async def TakeTopAdress():

    streetList = []
    #return streetList
    wallPostItemsText = VkTakeSummariesInPublic()  # 1 берем 10 публикаций и извлекаем из них список с записями
    for textContainingStreets in wallPostItemsText:  # 2 перебираем спискок с записями
        ExtrudeAddress(textContainingStreets, streetList)  # 3 передаем ссылку на пустой список улиц
    # print(streetList)

    D = defaultdict(list)
    # print(D)
    for i, item in enumerate(streetList):
        D[item].append(i)

    print(D)
    D = {k: len(v) for k, v in D.items() if len(v) > 1}
    print(D)
    return D
    # Нужен list формата ['улица':'рейтинг','улица':'рейтинг']
    # Почти готов
if __name__ == '__main__':
   print(TakeTopAdress())















