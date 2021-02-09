print('-----ENCODE-DECODE-----')
s = 'cafe'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode())

print('-----BYTES-BYTEARRAY-----')
cafe = bytes('cafe', encoding='utf-8')
print(cafe)
print(cafe[0])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print('bytearray(cafe)[0]', cafe_arr[0])
print('bytearray(cafe)[3]', cafe_arr[:3])   #возвращает последовательность

print('-----UNICODE-----')
print("error = 'replace'", "error = 'ignore'",
      'Chardet for identify encoding', 'unicodedata.normilize',
      'regex by str(r\') and bytes(rb\')',
      'УКАЗАТЬ КОДИРОВКУ В НАЧАЛЕ ФАЙЛА', sep='\n')

