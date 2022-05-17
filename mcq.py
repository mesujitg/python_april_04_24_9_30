questions = [
    'What is area of Nepal?',
    'Who is the first prime minister of Nepal?',
    'Population of Nepal acc. to Census 2078 is:',
    'What is the height of Mt. Everest?',
    'Number of Provinces in Nepal:'
]

answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']

# options = [
#     {'a':'147818 sq km', 'b':'157181 sq km', 'c':'147181 sq km', 'd':'157818 sq km'},
#     {'a':'Bhimsen Thapa', 'b':'Bhakti Thapa', 'c':'Kalu Pande', 'd':'Janga B Rana'},
#     {'a':'21,940,000', 'b':'24,110,000', 'c':'21,490,000', 'd':'29,140,000'},
#     {'a':'8884.4 m', 'b':'8848.8 m', 'c':'8848.4 m', 'd':'8884.8 m'},
#     {'a':'5', 'b':'6', 'c':'7', 'd':'8'}
# ]

options = [
    ['147818 sq km', '157181 sq km', '147181 sq km', '157818 sq km'],
    ['Bhimsen Thapa', 'Bhakti Thapa', 'Kalu Pande', 'Janga B Rana'],
    ['21,940,000', '24,110,000', '21,490,000', '29,140,000'],
    ['8884.4 m', '8848.8 m', '8848.4 m', '8884.8 m'],
    ['5', '6', '7', '8']
]

choices = {'a':0, 'b':1, 'c':2, 'd':3}

q_no = 0
score = 0


def show_qn_options():
    global q_no, score
    print(q_no+1, '.', questions[q_no])
    # for op in options[q_no]:
    #     print(op, ')', options[q_no][op])
    print('a)', options[q_no][0])
    print('b)', options[q_no][1])
    print('c)', options[q_no][2])
    print('d)', options[q_no][3])

    ans = input('Choose a/b/c/d: ')

    if ans not in ['a', 'b', 'c', 'd']:
        print('Wrong Input')
        ans = input('Choose a/b/c/d: ')
    
    # if options[q_no][ans] == answers[q_no]:
    #     score += 1

    if options[q_no][choices[ans]] == answers[q_no]:
        score += 1
    
    if q_no < len(questions)-1:
        q_no += 1
        show_qn_options()
    else:
        print('Your Score is: ', score)

show_qn_options()