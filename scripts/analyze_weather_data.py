import pandas as pd

# 파일 읽기
df = pd.read_json("./data/processed/processed_weather_20250429.json")

# (1) 평균/최대/최소 기온 (날씨별)
agg_temp_by_weather = df.groupby('weather_description')['temperature_celsius'].agg(['mean', 'max', 'min']).reset_index()
print("=== 날씨별 평균/최대/최소 기온 ===")
print(agg_temp_by_weather)

# (2) 'clear sky' & 15도 이상 필터링
clear_and_warm = df[(df['weather_description'] == 'clear sky') & (df['temperature_celsius'] >= 15)]
print("=== 맑고 따뜻한 날만 ===")
print(clear_and_warm)

# (3) 'high' / 'low' 온도 범주 컬럼 생성
df['temp_category'] = df['temperature_celsius'].apply(lambda x: 'high' if x >= 25 else 'low')
print("=== 고온/저온 분류 ===")
print(df[['temperature_celsius', 'temp_category']])

# (4) 온도 범주별 평균 습도
avg_humidity_by_category = df.groupby('temp_category')['humidity'].mean().reset_index()
print("=== 고온/저온별 평균 습도 ===")
print(avg_humidity_by_category)