


from datetime import datetime
def countUserLogin(logs):
    def custom_sort(time):
        return datetime.strptime(time[1], )
    arr=[]
    for ele in logs:
        if ele[2]=='ERROR'or ele[2]=='CRITICAL':arr.append(ele)

    arr= sorted(arr, key=custom_sort)
    return arr
