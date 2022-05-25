days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
        'Saturday']

# num = input('Enter a number')

# if not num.isdigit():
#     print('Invalid number')
# else:
#     num = int(num)

#     if num < 0 or num > 7:
#         print('invalid')
#     else:
#         print(days[num-1])

def show_day():
    try:
        num = int(input('Enter a number'))
        # print(num/0)
        if num < 0 or num > 7:
            print('invalid')
        else:
            print(days[num-1])
    except Exception as e:
        print(e)
    finally:
        show_day()


show_day()
