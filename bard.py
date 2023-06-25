from bardapi import Bard

token = input("Input Google Bard Token: ")

bard = Bard(token)

while True:
    question = input("質問を入力：")
    if question != "-1":
        answer = bard.get_answer(question)
        print(answer)
    else:
        break
