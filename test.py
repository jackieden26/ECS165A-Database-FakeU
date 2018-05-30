import csv

path = "/Users/jackie/Desktop/Grades/1990_Q3.csv"
                                    #duplicate_test
                                    #1989_Q4.csv

# with open (path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for line in csv_reader:
#         print(line)
file = open(path,'r')
reader = csv.reader(file)
listreader = list(reader)

#this is list of 4 relations tuples, tl = tuple list, ts = tuple strings
#each element is a tuple string
studentstl = []
studentsts = ''
taketl = []
takets = ''
coursestl = []
coursests = ''
meetingtl = []
meetingts = ''

sidl = []  #check whether we are inserting duplicate student relation
           #if there is duplicate, we should not insert it again in relation

cidtermtl = []  #check whether a course cid and term appear twice
                #which means that this is a summer 2 class
lenlist = len(listreader)
summer = 0
gradedic = {'A+':4.000,'A':4.000,'A-':3.700,'B+':3.300,'B':3.000,'B-':2.700, \
            'C+':2.300,'C':2.000,'C-':1.700,'D+':1.300,'D':1.000,'D-':0.700, \
            'F':0.000}

# header = next(reader)
i = 0
while i < lenlist:
    if i == 0:
        if listreader[0] != ['']:
            print("file begining doesn't begin with empty \
                    line, which I thought it should")

        i += 1
        continue

    if i > 0:
        lastrow = listreader[i-1]
    row = listreader[i]
    if i < lenlist - 1 :
        nextrow = listreader[i+1]


    # currentrow is CID,TERM,SUBJ...
    if row[0] =='CID':

        summer = 0 #set summer to 0 to avoid mistakes,
                   #we change summer only in CID-if

        #trying to find whether this class has student
        findnextseat = i
        while findnextseat < lenlist:
            if listreader[findnextseat][0] != 'SEAT':
                findnextseat += 1

            #now findnextseat is the line that is SEAT,SID...
            else:
                break

            #reach the end of file, and it ends with a class has no student
        if findnextseat + 1 == lenlist:
            print("this is the end of the file, and this class class has no student")
            break

        #this is not the last class in file, and this class has no student,
        #we set i to the nextline of the SEAT,SID...
        elif listreader[findnextseat + 1] == ['']:
            i = findnextseat + 1
            continue

        else: #this course has student, it is a valid class
            cid = nextrow[0]
            term = nextrow[1]
            subj = nextrow[2]
            crse = nextrow[3]
            sec = nextrow[4]
            units = nextrow[5]


            cidterm = cid+term
            if cidterm in cidtermtl:
                print("we have a summer 2 now")
                summer = 1
            else:
                cidtermtl.append(cidterm)


            coursestuple = (cid, term, crse, sec, units, subj,summer)
            coursestl.append(coursestuple)


            i += 1
            continue

    # currentrow is INSTRUCTOR(S),TYPE,DAYS...
    elif row[0] == 'INSTRUCTOR(S)':

        #j represents the next total empty line
        j = i
        while j < lenlist:
            if listreader[j] != ['']:
                j += 1
            else:
                break

        # no instructor at all, totally empty
        # because CID-IF will jump through the class who has no student,
        # then in this if, there has to be student below,even
        # there is no instructor at all (no type, no days...)
        # which actually should not happen, because no student can have no instructor
        if j == i+1 :
            i += 2
            print("we shouldn't go into here because no student have no instructor")
            continue

        #at least one instructor line
        else:
            instructors = nextrow[0]

            #We want to know what is this course
            #we want tot get CID, TERM, SUMMER to create meeting tuples
            lastlastrow = listreader[i-2]
            cid = lastlastrow[0]
            term = lastlastrow[1]

            #this line(i+1) has no instructor, which means this class's instructors
            #is somewhere above
            #we assume that there are students below because we are supposed to
            #jump the whole block when it has no student in courses-if
            if instructors == '':
                for backfindc in range(i-1,0,-1):
                    if listreader[backfindc][0] != 'CID':
                        continue
                    else: #backfindc is the line CID,TERM...
                        if listreader[backfindc + 1][2] == lastlastrow[2]   \
                        and listreader[backfindc + 1][3] == lastlastrow[3] \
                        and listreader[backfindc+4][0] != '':
                            instructors = listreader[backfindc+4][0]
                            break
                        else:
                            continue
            lastinstructors = instructors
            if lastinstructors == '':
                print("we cannot find previous instructor, so I set it to empty string")


            #l represents possible instructors line
            #j should represent next empty line
            for l in range(i+1,j):
                lcurrentrow = listreader[l]
                if lcurrentrow[0] == '':
                    instructors = lastinstructors
                else:
                    instructors = lcurrentrow[0]
                    lastinstructors = instructors
                mtype = lcurrentrow[1]
                days = lcurrentrow[2]
                time = lcurrentrow[3]
                build = lcurrentrow[4]
                room = lcurrentrow[5]

                meetingtuple = (cid,time,build,days,instructors,mtype, \
                        room,term,summer)
                meetingtl.append(meetingtuple)

            i = j + 1
            continue





    #i/currentrow is SEAT,SID...
    elif row[0] == 'SEAT':
        #we want to make sure that this line follows by
        #non empty student information
        if i == lenlist -1 :
            print("we reach end of file in student if-block ")
            break
        elif nextrow == ['']:
            print("We are suppposed to jump the empty \
                student block, but we failed to do so")
            i += 1
            continue

        else: #now we know that nextrow has at least one valid student information

            #we need to find snextemptyline (studentnextemptyline)
            #after student block
            snextemptyline = i
            while snextemptyline < lenlist:
                if listreader[snextemptyline] != ['']:
                    snextemptyline += 1
                else:
                    break

            for m in range(i+1,snextemptyline):
                mcurrentrow = listreader[m]
                seat = mcurrentrow[0]
                sid = mcurrentrow[1]
                surname = mcurrentrow[2]
                prefname = mcurrentrow[3]
                level = mcurrentrow[4]
                units = mcurrentrow[5]
                sclass = mcurrentrow[6]  #avoid using keyword class
                major = mcurrentrow[7]
                grade = mcurrentrow[8]
                status = mcurrentrow[9]
                email = mcurrentrow[10]

                if sid in sidl:
                    pass
                else:
                    sidl.append(sid)
                    studentstuple = (sid,status,prefname,surname,email)
                    studentstl.append(studentstuple)

                #we need to find cid,term,ngrade
                #and make sure units is within the course units range

                #i is the line SEAT,SID...
                #so we need to find the line of CID,TERM to get info
                backcourserownumber = 0
                for backfindcourse in range(i-1,0,-1):
                    if listreader[backfindcourse][0] != 'CID':
                        continue
                    else:
                        backcourserownumber = backfindcourse

                backcourserow = listreader[backcourserownumber]
                cid = backcourserow[0]
                term = backcourserow[1]
                unitsrange = backcourserow[5]



                if grade in gradedic:
                    ngrade = gradedic[grade]
                else:
                    ngrade = -1

                taketuple = (sid,cid,term,major,seat,sclass,level,units,\
                        grade,ngrade,summer)
                taketl.append(taketuple)




            i += 1
            continue




    else:
        i += 1
        continue





coursests = str(coursestl).strip('[]')
meetingts = str(meetingtl).strip('[]')
studentsts = str(studentstl).strip('[]')
takets = str(taketl).strip('[]')

# adding more comment




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
