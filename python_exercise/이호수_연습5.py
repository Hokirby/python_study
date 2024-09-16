# # 041

# ticker = "btc_krw"
# ticker = ticker.upper() # 문자열 대문자로 변환 메서드
# print(ticker)

# # 042

# ticker = "BTC_KRW"
# ticker = ticker.lower() # 문자열 소문자로 변환 메서드
# print(ticker)

# # 043

# a = "hello"
# a = a.capitalize() # Hello
# print(a)

# # 044

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx")) # 문자열이 특정단어로 끝나는지 확인 True/False

# # 045

# file_name = "보고서.xlsx"
# print(file_name.endswith(("xlsx","xsl"))) # 여러 패턴 확인시 튜플로 입력

# # 046

# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020")) # 문자열이 특정단어로 시작하는지 확인  True/False

# # 047

# a = "hello world"
# print(a.split()) # 기본적으로 공백을 기준으로 분리
# print(a.split(" "))

# # 048

# ticker = "btc_krw"
# print(ticker.split("_"))

# # 049

# date = "2020-05-01"
# print(date.split("-"))

# # 050

# data = "039490     "
# print(data.rstrip()) # 오른쪽 공백 제거
# print(data.strip()) # 앞뒤 공백 제거