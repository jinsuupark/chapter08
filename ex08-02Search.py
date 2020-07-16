#검색

def main():
    s = "python prgramming"
    print(len(s))
    print(s.find('o'))
    print(s.rfind('o'))
    print(s.index('r'))
    print(s.count('n'))
    print(s.find('q')) # 없는경우 -1 출력 확인
    #print(s.index('j')) #없는경우 오류 발생
    s = "hello"

    print(s[2])
    # s[2] = 'L'                     -> 오류 쓰기가 안된다. 문자열은 *불변 객체. 수정불가. 값을 통째로 바꿀수는있다. 부분변화X
    print(s[2])



main()