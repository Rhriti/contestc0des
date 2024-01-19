from collections import defaultdict
from datetime import datetime

def countUserLogin(logs):
    # Create a defaultdict to count logins for each (ID, date) pair
    user_login_count = defaultdict(int)
    
    # Iterate through the log entries and count logins
    for log in logs:
        user_id, date = log[0],log[2]  # Assuming log is in the format ['ID', 'date', 'time']
        user_login_count[(user_id, date)] += 1

    # Define a sorting function to sort by date
    def csort(log_entry):
        return datetime.strptime(log_entry[1], "%Y-%m-%d")

    # Create a list of [ID, date, count] entries
    result = []
    for (user_id, date), count in user_login_count.items():
        result.append([user_id, date, count])

    # Sort the list first by ID and then by date
    result = sorted(result, key=lambda x: (x[0], csort(x)))
    return result