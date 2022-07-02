# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
CHOSUNG_DICT = {'ㄱ':2, 'ㄲ':4, 'ㄴ':2, 'ㄷ':3, 'ㄸ':6, 'ㄹ':5, 'ㅁ':4, 'ㅂ':4, 'ㅃ':8, 'ㅅ':2, 'ㅆ':4, 'ㅇ':1, 'ㅈ':3, 'ㅉ':6, 'ㅊ':4, 'ㅋ':3, 'ㅌ':4, 'ㅍ':4, 'ㅎ':3}
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JUNGSUNG_DICT = {'ㅏ':2, 'ㅐ':3, 'ㅑ':3, 'ㅒ':4, 'ㅓ':2, 'ㅔ':3, 'ㅕ':3, 'ㅖ':4, 'ㅗ':2, 'ㅘ':4, 'ㅙ':5, 'ㅚ':3, 'ㅛ':3, 'ㅜ':2, 'ㅝ':4, 'ㅞ':5, 'ㅟ':3, 'ㅠ':3, 'ㅡ':1, 'ㅢ':2, 'ㅣ':1}
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JONGSUNG_DICT = {' ':0, 'ㄱ':2, 'ㄲ':4, 'ㄳ':4, 'ㄴ':2, 'ㄵ':5, 'ㄶ':5, 'ㄷ':3, 'ㄹ':5, 'ㄺ':7, 'ㄻ':9, 'ㄼ':9, 'ㄽ':7, 'ㄾ':9, 'ㄿ':9, 'ㅀ':8, 'ㅁ':4, 'ㅂ':4, 'ㅄ':6, 'ㅅ':2, 'ㅆ':4, 'ㅇ':1, 'ㅈ':3, 'ㅊ':4, 'ㅋ':3, 'ㅌ':4, 'ㅍ':4, 'ㅎ':3}

#입력받은 음운분리
def korean_to_be_englished(korean_word):
    """음운 분리 코드(출처 : https://frhyme.github.io/python/python_korean_englished/)"""
    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함.
        if '가' <= w <= '힣':
            ## 588개 마다 초성이 바뀜.
            ch1 = (ord(w) - ord('가')) // 588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588 * ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588 * ch1) - 28 * ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

def name_index_num(names):
    """음운의 획수 확인해서 음절의 획수를 리스트로 리턴, 글자를 한글자씩 잘라서 리스트로 리턴"""
    name_index=list(str(names))
    eum_un = korean_to_be_englished(names)
    name_values=[]
    for i in range(len(eum_un)):
        namevalue = []
        for j in range(len(eum_un[i])):
            try:
                val1=CHOSUNG_DICT[eum_un[i][j]]
                namevalue.append(val1)
            except KeyError:
                try:
                    val2 = JUNGSUNG_DICT[eum_un[i][j]]
                    namevalue.append(val2)
                except KeyError:
                    val3 = JONGSUNG_DICT[eum_un[i][j]]
                    namevalue.append(val3)
        name_values.append(sum(namevalue))
    return name_values, name_index

def name_mix(man, women):
    a=name_index_num(man)
    b=name_index_num(women)
    name1=a[1]
    name2=b[1]
    name1.insert(1,name2[0])
    name1.insert(3,name2[1])
    try:
        name1.insert(5, name2[2])
    except:
        pass
    try:
        name1.insert(7, name2[3])
    except:
        pass
    return name1

def num_mix(man, women):
    a=name_index_num(man)
    b=name_index_num(women)
    number1=a[0]
    number2=b[0]
    number1.insert(1,number2[0])
    number1.insert(3,number2[1])
    try:
        number1.insert(5,number2[2])
    except:
        pass
    try:
        number1.insert(7,number2[3])
    except:
        pass
    return number1

def name_taro(man, woman):
    result_name_mix = name_mix(man, woman)
    result_num_mix = num_mix(man, woman)
    if len(result_num_mix)==4:
        print(result_name_mix[0],result_name_mix[1], result_name_mix[2], result_name_mix[3])
        print(result_num_mix[0],result_num_mix[1],result_num_mix[2],result_num_mix[3])
        first_calc1 = result_num_mix[0] + result_num_mix[1]
        first_calc2 = result_num_mix[1] + result_num_mix[2]
        first_calc3 = result_num_mix[2] + result_num_mix[3]
        if first_calc1 >= 10:
            first_calc1 -= 10
        if first_calc2 >= 10:
            first_calc2 -= 10
        if first_calc3 >= 10:
            first_calc3 -= 10
        print("|/|/|/")
        print(first_calc1, first_calc2, first_calc3)
        second_calc1 = first_calc1 + first_calc2
        second_calc2 = first_calc2 + first_calc3
        if second_calc1 == 10 and second_calc2 == 10:
            second_calc1 = 10
        elif second_calc1 >= 10:
            second_calc1 -= 10
        if second_calc1 == 10 and second_calc2 == 10:
            second_calc2 = 0
        elif second_calc2 >= 10:
            second_calc2 -= 10
        print("|/|/")
        print(second_calc1, second_calc2)
        result = 10 * second_calc1 + second_calc2
        return result
    elif len(result_num_mix)==5:
        print(result_name_mix[0],result_name_mix[1], result_name_mix[2], result_name_mix[3], result_name_mix[4])
        print(result_num_mix[0],result_num_mix[1],result_num_mix[2],result_num_mix[3],result_num_mix[4])
        first_calc1 = result_num_mix[0] + result_num_mix[1]
        first_calc2 = result_num_mix[1] + result_num_mix[2]
        first_calc3 = result_num_mix[2] + result_num_mix[3]
        first_calc4 = result_num_mix[3] + result_num_mix[4]
        if first_calc1 >= 10:
            first_calc1 -= 10
        if first_calc2 >= 10:
            first_calc2 -= 10
        if first_calc3 >= 10:
            first_calc3 -= 10
        if first_calc4 >= 10:
            first_calc4 -= 10
        print("|/|/|/|/")
        print(first_calc1, first_calc2, first_calc3, first_calc4)
        second_calc1 = first_calc1 + first_calc2
        second_calc2 = first_calc2 + first_calc3
        second_calc3 = first_calc3 + first_calc4
        if second_calc1 >= 10:
            second_calc1 -= 10
        if second_calc2 >= 10:
            second_calc2 -= 10
        if second_calc3 >= 10:
            second_calc3 -= 10
        print("|/|/|/")
        print(second_calc1, second_calc2, second_calc3)
        third_calc1 = second_calc1 + second_calc2
        third_calc2 = second_calc2 + second_calc3
        if third_calc1 == 10 and third_calc2 == 10:
            third_calc1 = 10
        elif third_calc1 >= 10:
            third_calc1 -= 10
        if third_calc1 == 10 and third_calc2 == 10:
            third_calc2 = 0
        elif third_calc2 >= 10:
            third_calc2 -= 10
        print("|/|/")
        print(third_calc1, third_calc2)
        result = 10 * third_calc1 + third_calc2
        return result
    elif len(result_num_mix)==6:
        print(result_name_mix[0],result_name_mix[1], result_name_mix[2], result_name_mix[3], result_name_mix[4], result_name_mix[5])
        print(result_num_mix[0],result_num_mix[1],result_num_mix[2],result_num_mix[3],result_num_mix[4],result_num_mix[5])
        first_calc1 = result_num_mix[0] + result_num_mix[1]
        first_calc2 = result_num_mix[1] + result_num_mix[2]
        first_calc3 = result_num_mix[2] + result_num_mix[3]
        first_calc4 = result_num_mix[3] + result_num_mix[4]
        first_calc5 = result_num_mix[4] + result_num_mix[5]
        if first_calc1 >= 10:
            first_calc1 -= 10
        if first_calc2 >= 10:
            first_calc2 -= 10
        if first_calc3 >= 10:
            first_calc3 -= 10
        if first_calc4 >= 10:
            first_calc4 -= 10
        if first_calc5 >= 10:
            first_calc5 -= 10
        print("|/|/|/|/|/")
        print(first_calc1, first_calc2, first_calc3, first_calc4, first_calc5)
        second_calc1 = first_calc1 + first_calc2
        second_calc2 = first_calc2 + first_calc3
        second_calc3 = first_calc3 + first_calc4
        second_calc4 = first_calc4 + first_calc5
        if second_calc1 >= 10:
            second_calc1 -= 10
        if second_calc2 >= 10:
            second_calc2 -= 10
        if second_calc3 >= 10:
            second_calc3 -= 10
        if second_calc4 >= 10:
            second_calc4 -= 10
        print("|/|/|/|/")
        print(second_calc1, second_calc2, second_calc3, second_calc4)
        third_calc1 = second_calc1 + second_calc2
        third_calc2 = second_calc2 + second_calc3
        third_calc3 = second_calc3 + second_calc4
        if third_calc1 >= 10:
            third_calc1 -= 10
        if third_calc2 >= 10:
            third_calc2 -= 10
        if third_calc3 >= 10:
            third_calc3 -= 10
        print("|/|/|/")
        print(third_calc1, third_calc2, third_calc3)
        Fourth_calc1 = third_calc1 + third_calc2
        Fourth_calc2 = third_calc2 + third_calc3
        if Fourth_calc1 == 10 and Fourth_calc2 == 10:
            Fourth_calc1 = 10
        elif Fourth_calc1 >= 10:
            Fourth_calc1 -= 10
        if Fourth_calc1 == 10 and Fourth_calc2 == 10:
            Fourth_calc2 = 0
        elif Fourth_calc2 >= 10:
            Fourth_calc2 -= 10
        print("|/|/")
        print(Fourth_calc1, Fourth_calc2)
        result = 10 * Fourth_calc1 + Fourth_calc2
        return result
    elif len(result_num_mix)==7:
        print(result_name_mix[0], result_name_mix[1], result_name_mix[2], result_name_mix[3], result_name_mix[4], result_name_mix[5], result_name_mix[6])
        print(result_num_mix[0], result_num_mix[1], result_num_mix[2], result_num_mix[3], result_num_mix[4], result_num_mix[5], result_num_mix[6])
        first_calc1 = result_num_mix[0] + result_num_mix[1]
        first_calc2 = result_num_mix[1] + result_num_mix[2]
        first_calc3 = result_num_mix[2] + result_num_mix[3]
        first_calc4 = result_num_mix[3] + result_num_mix[4]
        first_calc5 = result_num_mix[4] + result_num_mix[5]
        first_calc6 = result_num_mix[5] + result_num_mix[6]
        if first_calc1 >= 10:
            first_calc1 -= 10
        if first_calc2 >= 10:
            first_calc2 -= 10
        if first_calc3 >= 10:
            first_calc3 -= 10
        if first_calc4 >= 10:
            first_calc4 -= 10
        if first_calc5 >= 10:
            first_calc5 -= 10
        if first_calc6 >= 10:
            first_calc6 -= 10
        print("|/|/|/|/|/|/")
        print(first_calc1,first_calc2,first_calc3,first_calc4,first_calc5,first_calc6)
        second_calc1 = first_calc1 + first_calc2
        second_calc2 = first_calc2 + first_calc3
        second_calc3 = first_calc3 + first_calc4
        second_calc4 = first_calc4 + first_calc5
        second_calc5 = first_calc5 + first_calc6
        if second_calc1 >= 10:
            second_calc1 -= 10
        if second_calc2 >= 10:
            second_calc2 -= 10
        if second_calc3 >= 10:
            second_calc3 -= 10
        if second_calc4 >= 10:
            second_calc4 -= 10
        if second_calc5 >= 10:
            second_calc5 -= 10
        print("|/|/|/|/|/")
        print(second_calc1, second_calc2, second_calc3, second_calc4, second_calc5)
        third_calc1 = second_calc1 + second_calc2
        third_calc2 = second_calc2 + second_calc3
        third_calc3 = second_calc3 + second_calc4
        third_calc4 = second_calc4 + second_calc5
        if third_calc1 >= 10:
            third_calc1 -= 10
        if third_calc2 >= 10:
            third_calc2 -= 10
        if third_calc3 >= 10:
            third_calc3 -= 10
        if third_calc4 >= 10:
            third_calc4 -= 10
        print("|/|/|/|/")
        print(third_calc1, third_calc2, third_calc3, third_calc4)
        Fourth_calc1 = third_calc1 + third_calc2
        Fourth_calc2 = third_calc2 + third_calc3
        Fourth_calc3 = third_calc3 + third_calc4
        if Fourth_calc1 >= 10:
            Fourth_calc1 -= 10
        if Fourth_calc2 >= 10:
            Fourth_calc2 -= 10
        if Fourth_calc3 >= 10:
            Fourth_calc3 -= 10
        print("|/|/|/")
        print(Fourth_calc1, Fourth_calc2, Fourth_calc3)
        fifth_calc1 = Fourth_calc1 + Fourth_calc2
        fifth_calc2 = Fourth_calc2 + Fourth_calc3
        if fifth_calc1 == 10 and fifth_calc2 == 10:
            fifth_calc1 = 10
        elif fifth_calc1 >= 10:
            fifth_calc1 -= 10
        if fifth_calc1 == 10 and fifth_calc2 == 10:
            fifth_calc2 = 0
        elif fifth_calc2 >= 10:
            fifth_calc2 -= 10
        print("|/|/")
        print(fifth_calc1, fifth_calc2)
        result = 10 * fifth_calc1 + fifth_calc2
        return result
    elif len(result_num_mix)==8:
        print(result_name_mix[0], result_name_mix[1], result_name_mix[2], result_name_mix[3], result_name_mix[4],
              result_name_mix[5], result_name_mix[6], result_name_mix[7])
        print(result_num_mix[0], result_num_mix[1], result_num_mix[2], result_num_mix[3], result_num_mix[4],
              result_num_mix[5], result_num_mix[6], result_num_mix[7])
        first_calc1 = result_num_mix[0] + result_num_mix[1]
        first_calc2 = result_num_mix[1] + result_num_mix[2]
        first_calc3 = result_num_mix[2] + result_num_mix[3]
        first_calc4 = result_num_mix[3] + result_num_mix[4]
        first_calc5 = result_num_mix[4] + result_num_mix[5]
        first_calc6 = result_num_mix[5] + result_num_mix[6]
        first_calc7 = result_num_mix[6] + result_num_mix[7]
        if first_calc1 >= 10:
            first_calc1 -= 10
        if first_calc2 >= 10:
            first_calc2 -= 10
        if first_calc3 >= 10:
            first_calc3 -= 10
        if first_calc4 >= 10:
            first_calc4 -= 10
        if first_calc5 >= 10:
            first_calc5 -= 10
        if first_calc6 >= 10:
            first_calc6 -= 10
        if first_calc7 >= 10:
            first_calc7 -= 10
        print("|/|/|/|/|/|/|/")
        print(first_calc1,first_calc2,first_calc3,first_calc4,first_calc5,first_calc6,first_calc7)
        second_calc1 = first_calc1 + first_calc2
        second_calc2 = first_calc2 + first_calc3
        second_calc3 = first_calc3 + first_calc4
        second_calc4 = first_calc4 + first_calc5
        second_calc5 = first_calc5 + first_calc6
        second_calc6 = first_calc6 + first_calc7
        if second_calc1 >= 10:
            second_calc1 -= 10
        if second_calc2 >= 10:
            second_calc2 -= 10
        if second_calc3 >= 10:
            second_calc3 -= 10
        if second_calc4 >= 10:
            second_calc4 -= 10
        if second_calc5 >= 10:
            second_calc5 -= 10
        if second_calc6 >= 10:
            second_calc6 -= 10
        print("|/|/|/|/|/|/")
        print(second_calc1, second_calc2, second_calc3, second_calc4, second_calc5, second_calc6)
        third_calc1 = second_calc1 + second_calc2
        third_calc2 = second_calc2 + second_calc3
        third_calc3 = second_calc3 + second_calc4
        third_calc4 = second_calc4 + second_calc5
        third_calc5 = second_calc5 + second_calc6
        if third_calc1 >= 10:
            third_calc1 -= 10
        if third_calc2 >= 10:
            third_calc2 -= 10
        if third_calc3 >= 10:
            third_calc3 -= 10
        if third_calc4 >= 10:
            third_calc4 -= 10
        if third_calc5 >= 10:
            third_calc5 -= 10
        print("|/|/|/|/|/")
        print(third_calc1, third_calc2, third_calc3, third_calc4, third_calc5)
        Fourth_calc1 = third_calc1 + third_calc2
        Fourth_calc2 = third_calc2 + third_calc3
        Fourth_calc3 = third_calc3 + third_calc4
        Fourth_calc4 = third_calc4 + third_calc5
        if Fourth_calc1 >= 10:
            Fourth_calc1 -= 10
        if Fourth_calc2 >= 10:
            Fourth_calc2 -= 10
        if Fourth_calc3 >= 10:
            Fourth_calc3 -= 10
        if Fourth_calc4 >= 10:
            Fourth_calc4 -= 10
        print("|/|/|/|/")
        print(Fourth_calc1, Fourth_calc2, Fourth_calc3, Fourth_calc4)
        fifth_calc1 = Fourth_calc1 + Fourth_calc2
        fifth_calc2 = Fourth_calc2 + Fourth_calc3
        fifth_calc3 = Fourth_calc3 + Fourth_calc4
        if fifth_calc1 >= 10:
            fifth_calc1 -= 10
        if fifth_calc2 >= 10:
            fifth_calc2 -= 10
        if fifth_calc3 >= 10:
            fifth_calc3 -= 10
        print("|/|/|/")
        print(fifth_calc1, fifth_calc2, fifth_calc3)
        sixth_calc1 = fifth_calc1 + fifth_calc2
        sixth_calc2 = fifth_calc2 + fifth_calc3
        if sixth_calc1 == 10 and sixth_calc2 == 10:
            sixth_calc1 = 10
        elif sixth_calc1 >= 10:
            sixth_calc1 -= 10
        if sixth_calc1 == 10 and sixth_calc2 == 10:
            sixth_calc2 = 0
        elif sixth_calc2 >= 10:
            sixth_calc2 -= 10
        print("|/|/")
        print(sixth_calc1, sixth_calc2)
        result = 10 * sixth_calc1 + sixth_calc2
        return result

if __name__ == "__main__":
    print("*" * 20, "이름 궁합 + (꽃별천지)", "*" * 20,"\n")
    while True:
        a = input("이름 궁합을 볼 사람(남자, 두글자 이상 네글자 이하) : ")
        b = input("이름 궁합을 볼 사람(여자, 두글자 이상 네글자 이하) : ")
        c = sum(name_index_num(a)[0])
        d = sum(name_index_num(b)[0])
        e = c+d
        if c%4==0:
            c_area="지옥"
        elif c%4==1:
            c_area="꽃나라"
        elif c%4==2:
            c_area="별나라"
        else:
            c_area="천국"
        if d % 4 == 0:
            d_area = "지옥"
        elif d % 4 == 1:
            d_area = "꽃나라"
        elif d % 4 == 2:
            d_area = "별나라"
        else:
            d_area = "천국"
        if e % 4 == 0:
            e_area = "지옥"
        elif e % 4 == 1:
            e_area = "꽃나라"
        elif e % 4 == 2:
            e_area = "별나라"
        else:
            e_area = "천국"
        print()
        print(a+"("+c_area+")",b+"("+d_area+")")
        print()
        if 4>=len(a)>=2 and 4>=len(b)>=2:
            print(a,b,"의 이름 궁합은",name_taro(a,b),"%","같이 하면","("+e_area+")")
        else:
            print()
            print("에러 : 이름을 잘못 입력했습니다.\n(지원하는 이름은 한글 두 글자에서 네 글자사이입니다)")
        try:
            print()
            c = int(input("-다시하려면 엔터키, 종료하려면 1을 누르고 엔터키를 누르세요 -\n"))
        except:
            c = 0
            print()
        if c=="1":
            break