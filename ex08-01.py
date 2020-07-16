#Sequence s
s = "python"
for c in s:
    print(c,end=",")

print()

#len() 문자열의 길이
for i in range(len(s)):
    print(s[i],end=',')

#슬라이싱 [begin:end:step] end값은 포함되지 않는다
# step default : +1 , 음수이면 뒤에서부터 진행
s = "0123456798"
print(s[2:5])
print(s[3:])
print(s[:4])


file = "20200101-104830.jpg"
print("촬영 날짜"+file[4:6]+"월"+file[6:8]+"일")
print("촬영 시간"+file[9:11]+"시"+file[11:13]+"분")
print("확장자 " + file[-3:])

dates = "월화수목금토일"
print(dates[::2])
print(dates[::-1])
print(type(dates[::2])) #Sclicing Return Value => Str

dates = "기러기"
if dates == dates[::-1]:
    print("회문입니다")
else:
    print("회문이 아닙니다")