import time
import datetime
import winsound
import os

count_pom = 0

winsound.Beep(440, 1000)

logging = []

date = datetime.datetime.today().strftime('%Y-%m-%d')

tot_poms = int(input("How many pomodoros do you want to do? "))
interval_time = int(input("How long should each pomodoro be? "))

while count_pom < tot_poms:
    count_pom += 1
    out = input("Start pomodoro number {}".format(count_pom))
    if out == "Exit":
        break
    print(datetime.datetime.now())
    start_t = datetime.datetime.now()
    if count_pom == tot_poms:
        print("LAST ONE! :)")
    time.sleep(interval_time*60)
    for i in range(2):
        winsound.Beep(440, 1000)
        time.sleep(1)
    print("Pomodoro number {} done".format(count_pom))
    tasks = input("What did you accomplish?\n")
    end_t = datetime.datetime.now()
    logging.append(end_t-start_t)
    logging.append(tasks)
    if "Exit" in tasks:
        break
    if count_pom == (tot_poms-1):
        print("On to your last pomodoro after this break! :)")
    if count_pom < tot_poms:
        print("Time for a break of 5 minutes! (at {})".format(datetime.datetime.now()))
        time.sleep(300)
        for i in range(5):
            winsound.Beep(440, 2000)
            time.sleep(1)

print("Finished a set of pomodoros!")
print("Break time for 15-30 minutes...")

if date+".txt" in os.listdir(os.getcwd()):
    f = open(date+".txt", "a")
else:
    f = open(date+".txt", "w")
f.write("Time\tTasks\n")
for i in range(len(logging)/2):
    step = i*2+1
    f.write("{}\t{}\n".format(logging[step-1], logging[step]))

f.close()
