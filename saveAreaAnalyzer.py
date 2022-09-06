#Сркипт анализирует безопасные зоны
from geopy.geocoders import Nominatim

def castAdressToCoordinates(adressList): #Кастуем адресс в координаты
    geolocator = Nominatim(user_agent="myApp")
    coordinatesList=[] #Список координат
    for adress in adressList:
        location = geolocator.geocode(adress, language="ru")
        coordinatesList.append(str(location.latitude, location.longitude))
        print(location.address)
        print((location.latitude, location.longitude))
    return coordinatesList


if __name__ == '__main__':
    # Адрес формата "Макеевка, ул. Садовая, 28"
    adressList=["Донецк, ул. Умова, 57", "Макеевка, ул. Садовая, 28"]
    print('PyCharm')