# Init
import numpy as np
import pandas as pd

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('max_columns', None)

# Get Data
df = pd.read_csv("data/naver_finance/2015_12.csv")
df = df.rename(columns={"ticker": "종목명"})

# DataFrame에서 Boolean Series 생성

## Series 비교
a = df['순이익률(%)'] > df['영업이익률(%)']
print(a.head()) 
print(a.sum()) # true 개수
print(a.mean()) # true 비율

## Boolean Series로 indexing
print(df[a].head()) # 순이익률이 영업이익률보다 큰 데이터만 출력
print(df[a].shape)

## 다중 Boolean Series
con1 = df['순이익률(%)'] > df['영업이익률(%)']
con2 = df['PBR(배)'] < 1
final_con = con1 & con2 # 기존 파이썬 문법과는 다르게 pandas는 &, |을 사용
print(df[final_con])
df.loc[final_con].head(2) 
df.loc[final_con, ['ROE(%)']].head(2) # loc로도 가져올 수 있다. iloc은 불가능.

# isin()
name_list = ['삼성전자', '현대건설', "삼성물산"]
# 위 이름에 해당하는 데이터를 가져오려면?
## 01. Multiple Boolean Series를 이용
cond1 = df['종목명'] == "삼성전자"
cond2 = df['종목명'] == "현대건설"
cond3 = df['종목명'] == "삼성물산"

final_con = cond1 | cond2 | cond3
df[final_con]

## 02. 종목명을 컬럼화 해서 row-wise indexing 이용
temp_df = df.set_index('종목명')
#temp_df['삼성전자']
print(temp_df.loc[['삼성전자', '현대건설', "삼성물산"],['PER(배)']])

## 03. isin 사용
cond = df['종목명'].isin(name_list)
df[cond]
### 예시
df[df['종목명'].isin(name_list)].head(2)
df.loc[df['종목명'].isin(name_list)].head(2)
df.loc[df['종목명'].isin(name_list), ['종목명', 'ROA(%)', 'ROE(%)']].head(2)


# all() vs any()
a = df[순이익률(%)] > 0
a.all() # 모두 true인가?
a.any() # 하나라도 true인가?
## 사용 예시
(df['순이익률(%)'] > 0).all()
(df['순이익률(%)'] > 0).any()
## 왜 False일까?
(df['순이익률(%)'] > -1000000).all() # 값 중에서 nan이 있어서 그럼.