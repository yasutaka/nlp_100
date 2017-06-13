'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''
# coding: utf-8

def cipher(text):
    cipher_text = ""

    for word in text:
        if word.islower():  #英小文字
            cipher_text += chr((219-ord(word)))
        else:
            cipher_text += word

    return cipher_text

# cipher関数呼ぶ
# 暗号化
cipher_text=cipher("I am a NLPer")
print(cipher_text)
# 複合化
decode_text=cipher(cipher_text)
print(decode_text)
