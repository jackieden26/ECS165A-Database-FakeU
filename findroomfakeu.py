import csv
import sys
import os
import fnmatch
import ntpath
#import psycopg2
# this function actually knows argv is blank, relative path, abs path and
# returns the absdir magically




expandterm = sys.argv[1]
expandcid = sys.argv[2]
expandstudent = sys.argv[3]


#we need to find each room's capacity first.
conn = psycopg2.connect(database="FakeUData")
print 'connect successful'
cursor=conn.cursor()


cursor.execute('''\
    WITH R1 AS(\
        SELECT meeting.term as term1, meeting.summer as summer1, meeting.cid as cid1, \
                courses.term as term2, courses.summer as summer2, courses.cid as cid2,\
                build,room,days,time,subj,crse \
        FROM Meeting, Courses \
        WHERE meeting.term = courses.term and meeting.summer = courses.summer and \
                meeting.cid = courses.cid )\
        \
        SELECT term1,summer1,cid1,build,room,days,time,subj,crse \
        FROM R1 ''')


allinfo = cursor.fetchall()

cursor.execute('''\
    WITH R1 AS (\
        SELECT meeting.term as term1, meeting.summer as summer1, meeting.cid as cid1, \
                courses.term as term2, courses.summer as summer2, courses.cid as cid2,\
                build,room,days,time,subj,crse \
        FROM Meeting, Courses \
        WHERE meeting.term = courses.term and meeting.summer = courses.summer and \
                meeting.cid = courses.cid), \
    \
    R2 AS ( \
        SELECT cid,term,summer,build,room, MAX(seat) as peoplepresent,subj,crse \
        FROM R1,Take \
        WHERE term1 = term and summer1 = summer and cid1 = cid \
        GROUP BY term,summer,cid,build,room,subj,crse),\
    \
    R4 AS (\
        SELECT  \
        FROM  R2, R2 R3\
        WHERE R2.TERM = R3.TERM AND R2.SUMMER = R3.SUMMER AND R2.),\

    \
    R5 AS (\
        SELECT




    ''')



capacityinfo = cursor.fetchall()





for allinforow in allinfo:
    if allinforow[0] = expandterm and allinforow[2] = expandcid
















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
