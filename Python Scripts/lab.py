import re
import operator
import csv

errors = {}
per_user = {}

with open('syslog.log') as file:
    for line in file:
        user = ""
        result = None
        result = re.search(r"ERROR .+", line)
        resultINFO = None
        resultINFO = re.search(r"INFO .+", line)
        just_error = re.search(r"ERROR (.* )", line)
        if result != None:
            Full_Result = result.group(0)
            error_string = just_error.group(0)
            user = re.search(r"(\(.*$)", Full_Result)
            user = user.group(0)
            cleanuser = re.search(r"[\w\.]+", user)
            user = cleanuser.group(0)
            if user not in per_user:
                per_user[user] = [0, 1]
            else:
                per_user[user][1] += 1
            if error_string not in errors:
                errors[error_string] = 1
            else:
                errors[error_string] += 1
        if resultINFO != None:
            Full_Result = resultINFO.group(0)
            user = re.search(r"(\(.*$)", Full_Result)
            user = user.group(0)
            cleanuser = re.search(r"[\w\.]+", user)
            user = cleanuser.group(0)
            if user not in per_user:
                per_user[user] = [1, 0]
            else:
                per_user[user][0] += 1

sortedUserList = dict(sorted(per_user.items(),key=operator.itemgetter(0)))

sortedErrors = dict(sorted(errors.items(),key=operator.itemgetter(1),reverse=True))

with open('error_message.csv','w') as error_report:
    writer = csv.writer(error_report)
    writer.writerow(["Error","Count"])
    for key,value in sortedErrors.items():
        writer.writerow([key,value])
with open('user_statistics.csv','w') as user_statistics:
    writer = csv.writer(user_statistics)
    writer.writerow(["Username","INFO","ERROR"])
    for key,value in sortedUserList.items():
        writer.writerow([key,value[0],value[1]])


