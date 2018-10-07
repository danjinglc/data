cards_list = []


def show_menue():
    print("*" * 80)
    print("欢迎使用名牌管理系统")
    print("1,新增名片")
    print("2.现实全部")
    print("3.查找名片")
    print("")
    print("0.推出系统")
    print("*" * 80)


def new_cards():
    print("=" * 80)
    print("新增名片")
    name_str = input("姓名：")
    phone_str = input("电话：")
    cards_dict = {"name": name_str, "phone": phone_str}
    cards_list.append(cards_dict)
    print(cards_dict)
    print("添加%s完成" % name_str)


def show_all():
    print("=" * 80)
    print("显示全部")
    if len(cards_list) == 0:
        print("还没有输入名片，请重新输入名片")
        return

    else:
        for name in ("姓名", "电话"):
            print(name, end="\t\t")
    print("")
    print("-" * 80)
    for card_dict in cards_list:
        print("%s\t\t%s" % (card_dict["name"],
                            card_dict["phone"]))


def search_card():
    print("*" * 80)
    print("查找名片")
    find_name = input("请输入要查找的名字：")
    for card_dict in cards_list:
        if find_name == card_dict["name"]:
            print("姓名\t\t电话")
            print("=" * 80)
            print("%s\t\t%s" % (card_dict["name"],
                                card_dict["phone"]))
        else:
            print("抱歉没有找到%s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    action_str = input("输入要执行的操作：【1】修改【2】删除")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名")
        find_dict["phone"] = input_card_info(find_dict["phone", "电话"])
        print("修改完成")
    elif action_str == "2":
        cards_list.remove(find_dict)
        print("删除完成")


def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
