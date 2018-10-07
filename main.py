import cards_tools
while  True:
    cards_tools.show_menue()
    action_str = input("请选择执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    if action_str in ["1","2","3","0"]:
        if action_str == "1":
            cards_tools.new_cards()
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()
        elif action_str == "0":
            print("欢迎再次使用【名片管理系统】")
            break
    else:
        print("您输入有误，请重新输入")
