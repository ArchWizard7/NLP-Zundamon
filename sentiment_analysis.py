from mlask import MLAsk
emotion_analyzer = MLAsk("-d 'C:/Program Files/MeCab/dic/ipadic'")
result = emotion_analyzer.analyze('行列 $A = {{3, 1}, {1, 3}}$ の固有値は 3 と 1 です。固有値の計算方法は、行列式 $|A - \lambda I| = 0$ を解くことです。この場合、行列式は $|A - \lambda I| = (\lambda - 3)(\lambda - 1) = 0$ となり、固有値は $\lambda = 3$ と $\lambda = 1$ となります。')

print(result)
print(result["emotion"])
