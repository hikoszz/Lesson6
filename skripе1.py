test_string = input("ВВедите строку: ")
print("Оригинальная строка : " + str(test_string))
res = test_string.encode('utf-8')
print("Преобразованная строка  : " + str(res) + ", type : " + str(type(res)))


s = b" \xf0\x9f\x8d\x95!" 
str1 = s.decode('UTF-8')
print("Давайте покушаем " + str1)