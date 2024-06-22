import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stisfy = pd.read_csv('연령대별문화.csv')
stisfy = pd.DataFrame(stisfy)

#print(stisfy)

gu = stisfy[['구분별(3)']]
문화시설2021 = stisfy[['문화환경만족도']]

index = np.arange(len(gu))

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.bar(index, 문화시설2021['문화환경만족도'], width = 0.5, color = 'black' )
plt.title('연령대별 문화시설 만족도', fontsize=20)

plt.xlabel('행정구역', fontsize=18)
plt.ylabel('만족도 점수', fontsize=18)

plt.xticks(index, gu['구분별(3)'], fontsize=10)
plt.ylim([0, 7])

mean_value = np.mean(문화시설2021.values)
plt.axhline(mean_value, color='red', linestyle='--', linewidth=2, label='평균')
plt.legend() 

plt.show()
