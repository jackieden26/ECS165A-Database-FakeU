import csv

path = "/Users/jackie/Desktop/Grades/1989_Q4.csv"


# with open (path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for line in csv_reader:
#         print(line)
file = open(path,'r')
reader = csv.reader(file)
listreader = list(reader)

# header = next(reader)
i = 0
while i < len(listreader):

    if i > 0:
        lastrow = listreader[i-1]
        if listreader[i] == ['']:
            print("We are traversing an empty line which is not first line")
    row = listreader[i]
    nextrow = listreader[i+1]



    if listreader[0] != ['']:
        print("file begining doesn't begin with empty \
        line, which I thought it should")
        i += 1

    # currentrow is CID,TERM,SUBJ...
    if row[0] = 'CID':

        #trying to find whether this class has student
        findnextseat = i
        while findnextseat < len(listreader):
            if listreader[findnextseat][0] != 'SEAT':
                findnextseat += 1
            else:
                findnextseat += 1
                if listreader[findnextseat] = '':
                    i = findnextseat + 1
                else:
                    cid = nextrow[0]
                    term = nextrow[1]
                    subj = nextrow[2]
                    crse = nextrow[3]
                    sec = nextrow[4]
                    units = nextrow[5]
                    i += 1
                    continue

    # currentrow is INSTRUCTOR(S),TYPE,DAYS...
    elif row[0] = 'INSTRUCTOR(S)':

        #j represents the next total empty line
        j = i
        while j < len(listreader):
            if listreader[j] != ['']:
                j += 1
            else:
                break

        # no instructor at all
        if j == i+1 :
            i += 2
            continue

        #at least one instructor line
        else:
            lastinstructors = nextrow[0]

            #l represents possible instructors line
            for l in range(i+1,j):
                lcurrentrow = listreader[l]
                if lcurrentrow[0] = '':
                    instructors = lastinstructors
                else:
                    instructors = lcurrentrow[0]
                    lastinstructors = instructors
                type = lcurrentrow[1]
                days = lcurrentrow[2]
                time = lcurrentrow[3]
                build = lcurrentrow[4]
                room = lcurrentrow[5]

            i = j + 1
            continue

    #i/currentrow is SEAT,SID...
    else:
        if currentrow[0] != SEAT:
            print("something wrong here, the first element \
                should be seat but it is not seat")

        #we make sure that this line is SEAT,SID...
        else:
            if nextrow = ['']:
                print("We are suppposed to jump the empty \
                    student block, but we failed to do so")
            else:

                #we need to find snextemptyline
                #after student block
                snextemptyline = i
                while snextemptyline < len(listreader):
                    if listreader[snextemptyline] != ['']:
                        snextemptyline += 1
                    else:
                        break


                











        # for l in range(i,j):
        #
        #
        #
        #
        #
        #
        # if j != i + 1 :
        #     instructorslist = []
        #     typelist = []
        #     dayslist = []
        #     timelist = []
        #     buildlist = []
        #     roomlist = []
        #
        #     #k is used to read every valid instructor line
        #     #if what it reads is empty string, it should be treated as null
        #     #not an empty line
        #     k = i
        #     while k < j:
        #         instructors = listreader[k+1][0]
        #         if instructors = '':
        #             if k = i:
        #                 instructors = ''
        #                 type = nextrow[1]
        #                 days = nextrow[2]
        #                 time = nextrow[3]
        #                 build = nextrow[4]
        #                 room = nextrow[5]
        #         instructorlist.append(instructors)
