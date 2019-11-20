from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],
        histogram.values(),
        8)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)]) #rotulos no eixo x em 0, 10, ... 100

plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas do Teste")
plt.savefig("bar_chart_02.png")