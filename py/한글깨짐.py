import matplotlib.pyplot as plt
from matplotlib import font_manager

# 한글 폰트 경로 설정
font_path = '한글 폰트 파일(.ttf) 경로'

# 폰트 이름 얻어오기
font_prop = font_manager.FontProperties(fname=font_path)
font_name = font_prop.get_name()

# 폰트 설정
plt.rcParams['font.family'] = font_name