def main():
    s = "Good morning. my love Kim. "
    print(s.lower())
    print(s.upper())
    print(s.swapcase())
    print(s.capitalize())
    print(s.title())
    print(s)

    #Strip 사용빈도 : 낮음
    s = '   angel   '
    print(s +"님")
    print(s.strip()+"님")
    print(s.lstrip()+'님')
    print(s.rstrip()+'님')
    print(s)

    #.Split 분할 사용빈도 높음
    #.split() default 는 공백
    #문자열 -> 리스트
    s = "짜장 짬뽕 탕수육"
    print(s.split())

    s2 = "서울->천안-> 대전 -> 대구 -> 부산"
    cities = s2.split("->")

    print(cities)

    for city in cities:
        city.strip()
        #변화안됨
        print(city)

    trabler='''
강나루 거너서
밀밭 길을

구름에 달 가듯이
가는 나그네
'''

    poet = trabler.splitlines()
    for line in poet:
        print(line.center(30))
    print(len(poet))


    s='-_-'
    print(s.join("대한민국"))

    #대체
    s = '독도는 일본땅. 대마도도도도도 일본땅'
    print(s)
    print(s.replace('일본', '한국'))
    print(s)

    message = '안녕하세요'
    print(message.center(30))
    print(message.ljust(30))
    print(message.rjust(30))

main()