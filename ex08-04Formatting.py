#포맷팅
price = 500
print("궁금하면 " + str(price) + "원!")

month = 8
day = 15
anni = "광복절"
print("%d월 %d일은 %s이다." %(month, day, anni))                  #파이썬 3에서는 비권장        2ver.



#포맷팅 자리수
value = 123
print("###%d###"%value)
print("###%5d###"%value)
print("###%10d###"%value)
print("###%-10d###"%value)
print("###%1d###"%value)

price = [30, 13500, 2000]
for p in price:
    print("가격: %d원"%p)
print()
for p in price:
    print("가격 : %7d원"%p)
print()
for p in price:
    print("가격 : %-7d원"%p)



f = 123.4567
print("%10f"%f)
print("%10.8f"%f)
print("%10.5f"%f)
print("%10.2f"%f)
print("%.2f"%123.126)

#포맷 권장사항 format Method

name = "한결"
age = 16
height = 162.5
print("이름:{}, 나이:{} 키 : {}".format(name,age,height))
print("이름:{:s}, 나이:{:d} 키 : {:f}".format(name,age,height))
print("이름:{:4s}, 나이:{:3d} 키 : {:.2f}".format(name,age,height))

print("이름:{2}, 나이:{1} 키 : {0}".format(height,age,name))
print("이름:{name}, 나이:{age} 키 : {height}".format(name = "진수",height = "180",age = "28"))

print(f"이름:{name}, 나이 : {age}, 키 :{height:.2f}")

#Dictionary
# boy = {"name":"길동","age":20,"height":160.9}
# print("이름:{0[name]}, 나이 : {0[age]}, 키 :{0[height]}".format(boy))
