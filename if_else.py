# score = 80
# if score > 70:
#     print("good")
# else:
#     print("try harder")


def greeting(lang):
    if lang == "th":
        print("sawadee")
    elif lang == "jp":
        print("konichiwa")
    elif lang == "kr":
        print("ann-yoong")
    else:
        print("hello")
greeting("kr")

def meet_req(eng,interview):
    if eng > 70 and interview > 80:
        return True
    else:
        return False
print (meet_req(80,60))