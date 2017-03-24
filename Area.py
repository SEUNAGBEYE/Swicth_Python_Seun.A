def find_area():  
    l = int(raw_input('Enter Length:'))
    b = int(raw_input('Enter Breadth:'))
    Area= l*b
    print ("The Area of the Rectangle is"), Area
    return Area, l, b
find_area()

get_area=Area, l, b=find_area()

print get_area
