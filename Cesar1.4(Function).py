def caesarCipher(letter):
  for i in letter:
    myASCII = ord(i)
    myEncoded_ASCII = myASCII + 2
    myEncoded_chr = chr(myEncoded_ASCII)
    print(myEncoded_chr, end='')


prompt = caesarCipher("neHADd")
