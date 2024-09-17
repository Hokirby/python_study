# # 021

# letters = 'python'
# print(letters[0],letters[2])

# # 022

# license_plate = "175허 9795"
# print(license_plate[5:9]) # 슬라이싱
# print(license_plate[5:]) # 끝 생략 가능
# print(license_plate[-4:]) # 뒤에서부터 매길 수있음 맨뒤:-1 부터 시작

# # 023

# string = "홀짝홀짝홀짝"

# print(string[0], end="")
# print(string[2], end="")
# print(string[4])

# print(string[0:6:2]) # 세번째에 step 설정 가능
# print(string[::2]) # 처음과 끝 모두 생략 가능

# print(string[0],string[2],string[4], sep="")

# # 024

# string = "PYTHON"

# num=0
# for i in range(-1,-7,-1):
#     print(string[i], end="")
# print(string[::-1])

# # 025

# phone_number = "010-1111-2222"

# # print(phone_number[0:3],phone_number[5:8],phone_number[9:13])

# phone_number = phone_number.replace("-"," ")
# print(phone_number)

# # 026

# phone_number=phone_number.replace("-","")
# print(phone_number)

# # 027

# url = "http://sharebook.kr"
# a=url.split(".")
# print(a[1])

# print(url[-2:])

# # 028

# lang = 'python'
# lang[0] = 'P'# TypeError : 문자열은 변경할 수 없다
# print(lang)

# # 029

# string = 'abcdfe2a354a32a'
# a = string.replace("a","A")
# print(a)

# # 030

# string = 'abcd'
# a=string.replace("b","B") # string 변수 자체는 변하지 않는다.
# print(string)
# print(a)