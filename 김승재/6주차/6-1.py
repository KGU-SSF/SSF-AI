while(1) :
    w = input("단어를 입력해주세요(종료 : exit)")
    if w == "exit" :
        break
    w_list = list(w)
    w_list_reverse = list(reversed(w_list))
    if w_list == w_list_reverse :
        print("TRUE")
    else :
       print("FALSE")
