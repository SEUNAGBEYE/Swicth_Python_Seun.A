def build_list(user_list):
        "This function manipulate the collected user_list"
        number_of_items = len(user_list)
        lenght_of_third_item = len(user_list[2])
        first_item_in_list = user_list[0]
        print 'Third item in list: ', user_list[2]
        user_list[2] = user_list[0] #replace value of item at index 2 with value at index 0
        print 'Third item in list after swap: ', user_list[2]
        user_list.append('new value here')
        print 'lenght of list is: ', number_of_items
        print 'Lenght of third item in list is: ', lenght_of_third_item
        print 'multiplication of the list lenght & third item list is: ',  number_of_items*lenght_of_third_item
user_list = ['seun','ibra','samuel','tolu']

build_list(user_list)
