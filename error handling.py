while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    #coding dibawah silahkan dicoba setelah run ini
    #except ZeroDivisionError:
        #print('please enter age higher than 0')
        #break
    else:
        print('thank you!')
        break
    #finally:
        #print('ok, i am finally done')
    #print('canyou hear me?')
