"""
    lba3
"""
COST_LIMIT = 10  # COST limit of current flow
STABLE_LIMIT = 0.92  # COST limit of current flow
MAX_COST = 3000  # the max total COST
POINT = 0  # amount of service
MAX_POINT = 14  # size of the matrix

USEFUL_DATA = [[0 for col in range(501)] for row in range(15)]
#store the index of limit_fit data
STABLE = [[0 for col in range(501)] for row in range(15)]
#store the Reliability of each option
COST = [[0 for col in range(501)] for row in range(15)]
#store the Price of each option
R = [[0.0 for col in range(MAX_COST + 1)] for row in range(MAX_POINT + 1)]
#total Reliability of each option
PATH = [[0 for coFl in range(MAX_COST + 1)] for row in range(MAX_POINT + 1)]
#record the state con
CHOOSE = [[0 for coFl in range(MAX_COST + 1)] for row in range(MAX_POINT + 1)]
#record the CHOOSE
ANS = [0 for row in range(15)]
KIND = [0 for row in range(15)]
#total number of KINDs of choice,config in my_filter function
P = []
BEST = -1
P1 = []
SC=[0.0]*2


def read_process(con):
    """read process""" 
    global P1 
    f_process = open("PROCESS.txt","r")
    fpp = f_process.readlines()
    for j in range(0, len(fpp[con])):
        if fpp[con][j].isalpha() == 1:
            P.append(fpp[con][j])
    f_process.close()
    P1 = sorted(set(P), key = P.index)
    return len(P1)


def read_reg(con):
    """read reg"""
    line = []
    limit_stable = ""
    limit_cost = ""
    f_req = open("REQ.txt","r")
    line = (f_req.readlines())[con]
    line = line.split(',')
    for j in range(0, 2):
        for i in range(0, len(line[j])):
            if line[j][i] in ".1234567890" and j == 0:
                limit_stable += line[j][i]
            elif line[j][i] in ".1234567890" and j == 1:
                limit_cost += line[j][i]
    f_req.close()
    SC[0] = (float)(limit_stable)
    SC[1] = (float)(limit_cost)

def read_service():
    """read_service"""
    temp = []
    f_service = open("SERVICE.txt","r")
    fss = f_service.readlines()
    for i in range(len(fss)):
        temp = fss[i].split(' ')
        STABLE[i/500+1][i % 500 + 1] = (float)(temp[2])
        COST[i/500+1][i % 500 + 1] = (int)((float)(temp[4])*100)

def data_filter():  
    """filter of useless data"""
#    print COST_LIMIT
    for i in range(0, 15):
        KIND[i] = 0
        for k in range(0, 501):
            if STABLE[i][k]  > 1e-8 + STABLE_LIMIT \
            and COST[i][k] < 1e-8 + COST_LIMIT * 100:
#            if STABLE[i][k] >= STABLE_LIMIT and COST[i][k] <= COST_LIMIT:
          #      print k
                USEFUL_DATA[i][KIND[i]] = k
                KIND[i] += 1
#    print COST[14]
def char2num(name):
    """change char to int"""
    return ord(name) - 64

def calculate():
    """dynamic programming"""
    for m in range(1, MAX_COST):  # initialize
        R[0][m] = 1  # initialize the first row
    for n in range(0, POINT + 1):
        R[n][0] = 0  # initialize the first column
    for i in range(1, POINT + 1):
        actv = char2num(P1[i - 1])
        for j in range(1, MAX_COST + 1):
            temp = 0
            CHOOSE[i][j] = -1
            for k in range(0, KIND[actv]):
            #find the max Reliability until now for the current prince
                my_type = USEFUL_DATA[actv][k]
                #find the 'k'th useful choice activity 'actv'
                if j > COST[actv][my_type] :
                    f = R[i - 1][j - COST[actv][my_type]] *\
                    STABLE[actv][my_type]
                else:
                    f = 0  # impossible KIND for current price
                if f > temp:
                    temp = f
                    PATH[i][j] = j - COST[actv][my_type]
                    #record source
                    CHOOSE[i][j] = my_type
            R[i][j] = temp
def give_flow():  
    """give the ANSwer"""
    temp = 0
    pre = 0
    for i in range(1, MAX_COST + 1):
        if 10000 * R[POINT][i] - i > temp and i <= 100 * COST_LIMIT\
        and R[POINT][i] >= STABLE_LIMIT:
            temp = 10000 * R[POINT][i] - i
            pre = i

    global BEST
    BEST = pre
    for i in range(POINT, 0, -1):
        actv = char2num(P1[i - 1])
        ANS[actv] = CHOOSE[i][pre]
        pre = PATH[i][pre]


def output():
    """output"""
    i = 0
    my_string = ""
    while i < len(P):
        my_string += " (" + P[i] + "-"
        my_string += str(ANS[char2num(P[i])])
        my_string += "," + P[i + 1] + "-"
        my_string += str(ANS[char2num(P[i + 1])])
        my_string += "),"
        i += 2
    print my_string
    print ("Reliability=%.2f, Cost=%.2f, Q=%.2f" % \
    (R[POINT][BEST], BEST / 100.0, R[POINT][BEST] - BEST/10000.0))

#  main code
read_service()
for times in range(0, 4):
    # t1 = time.clock()
    
    POINT = read_process(times)
    
    read_reg(times)
    COST_LIMIT = SC[1]
    STABLE_LIMIT = SC[0]
    MAX_COST = int(COST_LIMIT * 100)
    data_filter()
    # calculate part
    calculate()
    # show part
    give_flow()
    # t2 = time.clock()
    output()
    # print t1, t2, t2 - t1










