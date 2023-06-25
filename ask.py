from mlask import MLAsk
import json

emotion_analyzer = MLAsk("-d 'C:/Program Files/MeCab/dic/ipadic'")

text = input("文章を入力：")
result = emotion_analyzer.analyze(text)
json_string = json.dumps(result, ensure_ascii=False, indent=4)

print(result)
print(json_string)

