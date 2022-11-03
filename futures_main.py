####################
#   Future Main Program
####################

####################
#   Import Python Package
####################

import pandas as pd


# 읽어올 엑셀 파일 지정
filename = 'data.xlsx'

# 엑셀 파일 읽어 오기
df = pd.read_excel (filename, engine='openpyxl')

# 데이타 열 추가
df.insert (0, '평균')

# 엑셀 파일 내용 출력
print (df)

####################
#   End of Program
####################
