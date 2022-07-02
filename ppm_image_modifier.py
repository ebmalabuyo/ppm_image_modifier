#a
def negate_image(k):
    '''This function accepts the input image file object and the output 
    image file object as arguments. For each pixel element, it takes the 
    value, subtracts 255 from it and takes the absolute value of the result.
    '''
    #copying the header
    try:    
        f=open("text1.txt")
        print(f.read())
    except IOError:
        print("File missing!!!")
    except:
        print("Unexpected error")
    else:
        f.close()
    q = open(k, 'r')
    u = open("outputA.ppm", 'w')
    for i in range(3):
        u.write(q.readline())
    values = q.read()
    lst1 = values.split()
    new_lst1 = [int(lst1[h]) for h in range(0, len(lst1))]
    #operation
    result_lst = []
    for s in new_lst1:
        result = abs(s - 225)
        result_lst.append(result)
    str_lst = [str(x) for x in result_lst]
    #change integers back to strings
    sent = " ".join(str_lst)
    u.write(sent)   
    q.close()
    u.close()
    return u 

negate_image('ny.ppm')

#b 
def high_contrast_image(h):
    '''This function accepts the input image file object and the 
    output image file object as arguments. For each pixel element, if the 
    value is higher than 127, set it to 255 or else set it to zero.
    '''
    #copying header
    q = open(h, 'r')
    u = open("outputB.ppm", 'w')
    for i in range(3):
        u.write(q.readline())
    values = q.read()
    lst1 = values.split()
    new_lst2 = [int(lst1[h]) for h in range(0, len(lst1))]
    #operation
    for v in range(len(new_lst2)):
        if new_lst2[v] > 127:
            new_lst2[v] = 255
        else:
            new_lst2[v] = 0
    str_lst2 = [str(d) for d in new_lst2]
    #changing back to string and making output
    sent2 = " ".join(str_lst2)
    u.write(sent2)
    q.close()
    u.close()
    return u


high_contrast_image('ny.ppm')

#c
def gray_scale_image(h):
    '''This function accepts the input image file object and the 
    output image file object as arguments. For each element in a RGB 
    triplet (consecutive three elements), convert its value to the triplets 
    average
    '''
    #copying header
    q = open(h, 'r')
    u = open("outputC.ppm", 'w')
    for i in range(3):
        u.write(q.readline())
    values = q.read()
    lst1 = values.split()
    new_lst2 = [int(lst1[h]) for h in range(0, len(lst1))]
    #operation
    #goes through entire list
    index = 0 
    #adds up the three numbers
    cur_sum = 0
    #tracks when we have reached 3 numbers and then restarts curr_sum and average
    track = 0
    #goes back to start of index and adds averages (follows index but goes up by 3)
    tracker_to_add = 0
    while index < len(new_lst2):
        cur_sum += new_lst2[index]
        index += 1
        track += 1
        if track == 3:
            avg = round(cur_sum / 3)
            for number in range(tracker_to_add, tracker_to_add + 3):
                new_lst2[number] = avg
            tracker_to_add +=3
            av = 0
            cur_sum = 0 
            track = 0
    str_lst2 = [str(d) for d in new_lst2]
    #changing back to string and making output
    sent2 = " ".join(str_lst2)
    u.write(sent2)
    q.close()
    u.close()
    return u

gray_scale_image('ny.ppm')

   
#d 
def remove_red_image(h):
    '''This function accepts the input image file object and the 
    output image file object as arguments. This function sets all red values 
    to 0
    '''
    #copying header
    q = open(h, 'r')
    u = open("outputD.ppm", 'w')
    for i in range(3):
        u.write(q.readline())
    values = q.read()
    lst1 = values.split()
    new_lst2 = [int(lst1[h]) for h in range(0, len(lst1))]
    #operation
    for i in range(0,len(new_lst2),3):
        new_lst2[i] = 0
    str_lst2 = [str(d) for d in new_lst2] 
    #changing back to string and making output
    sent2 = " ".join(str_lst2)
    u.write(sent2)
    q.close()
    u.close()
    return u


remove_red_image('ny.ppm')
    
#e
def remove_green_image(h):
    '''This function accepts the input image file object and the 
    output image file object as arguments. This function sets all green values 
    to 0
    '''
    #copying header
    q = open(h, 'r')
    u = open("outputE.ppm", 'w')
    for i in range(3):
        u.write(q.readline())
    values = q.read()
    lst1 = values.split()
    new_lst2 = [int(lst1[h]) for h in range(0, len(lst1))]
    #operation
    for s in range(1, len(new_lst2),3):
         new_lst2[s] = 0
    str_lst2 = [str(d) for d in new_lst2]
    #changing back to string and making output
    sent2 = " ".join(str_lst2)
    u.write(sent2)
    q.close()
    u.close()
    return u

remove_green_image('ny.ppm')
 
#f
def remove_blue_image(h):
    '''This function accepts the input image file object and the 
    output image file object as arguments. This function sets all blue values 
    to 0
    '''
    #copying header
    q = open(h, 'r')
    u = open("outputF.ppm", 'w')
    for i in range(3):
        u.write(q.readline())
    values = q.read()
    lst1 = values.split()
    new_lst2 = [int(lst1[h]) for h in range(0, len(lst1))]
    #operation
    for da in range(2, len(new_lst2), 3):
        new_lst2[da] = 0
    str_lst2 = [str(d) for d in new_lst2]
    #changing back to strings and output
    sent2 = " ".join(str_lst2)
    u.write(sent2)
    q.close()
    u.close()
    return u

remove_blue_image('ny.ppm')