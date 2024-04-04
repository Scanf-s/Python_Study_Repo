def print_lengths(strArr) -> list:
    strlen = list()
    for str in strArr:
        strlen.append(f'{str}의 길이 : {len(str)}')
    return strlen

random_str = ["asdfoighja", "kihgfisfjg", "fjgio", "dijhfoasjhdiufja", "lkvnblsdijkfgb", "jfhngjk"]
print_lengths(random_str)