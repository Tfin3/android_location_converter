with open('2019JANUARY.json', 'rb') as f:
   while 1:
      byte_s = f.read(1)
      if not byte_s:
         break
      byte = byte_s[0]
      print(byte)