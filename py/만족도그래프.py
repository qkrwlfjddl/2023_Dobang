import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stisfy = pd.read_csv('문화환경만족도.csv')
stisfy = pd.DataFrame(stisfy)

#print(stisfy)

gu = stisfy[['구분별(3)']]
만족도2021 = stisfy[['2021_만족도']]
문화시설2021 = stisfy[['2021_문화시설']]

index = np.arange(len(gu))

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.bar(index, 만족도2021['2021_만족도'], width = 0.5, color = 'black' )
plt.title('2021 문화생활 만족도', fontsize=20)

plt.xlabel('행정구역', fontsize=18)
plt.ylabel('만족도 점수', fontsize=18)

plt.xticks(index, gu['구분별(3)'], fontsize=10)
plt.ylim([0, 15])

mean_value = np.mean(만족도2021.values)
plt.axhline(mean_value, color='red', linestyle='--', linewidth=2, label='평균')
plt.legend() 

plt.show()
