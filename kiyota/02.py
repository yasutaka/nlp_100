# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

# coding: utf-8

str1 = "パトカー"
str2 = "タクシー"
str3 = ""

for a,b in zip(str1,str2):
    #str3 = str3 + a + b
    str3 += a + b
print (str3)

# 参考
# print(''.join([a + b for a, b in zip(str1, str2)]))
