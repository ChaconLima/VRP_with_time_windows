from datetime import datetime
import csv

def data(time):
    h, m = str(time).split('.')
    h = float(h)
    m = float('0.'+ str(m))*60
    return str(int(h))+':'+str(int(m))+':00'


def reading(solution, distances, travelTime, timeWindowsLower, timeWindowsUpper, sink, source):

    now = datetime.now()
    with open('./out/'+str(now.strftime("%d-%m-%Y-%H:%M:%S"))+'.csv', 'w', newline='') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        dt = 0
        for k in solution:
            dtk = 0
            
            for i in range(len(solution[k])):
                if(solution[k][i]=='Source'):
                    solution[k][i] = source
                elif(solution[k][i]=='Sink'):
                    solution[k][i] = sink

            timeAcc = timeWindowsLower[solution[k][0]]

            spamwriter.writerow(['Rota_'+str(k)])
            for i in range(len(solution[k])-1):

                dtk+=distances[solution[k][i]][solution[k][i+1]]
                dt+= distances[solution[k][i]][solution[k][i+1]]

                spamwriter.writerow(['identifier',solution[k][i],'time',data(timeAcc)])
                timeAcc+= travelTime[solution[k][i]][solution[k][i+1]]
 
            spamwriter.writerow(['identifier',solution[k][len(solution[k])-1],'time',data(timeAcc)])
            spamwriter.writerow(['Distance [Km]',str(dtk)])
            
    return 