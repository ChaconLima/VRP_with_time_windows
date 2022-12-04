
TIME_WINDOWS_LOWER = 0
TIME_WINDOWS_UPPER = 1 

def create(data):
    time_lower = {}
    for point in range(len(data)-1):
        if(str(data[point][TIME_WINDOWS_LOWER])!='nan'):
            h, m, s = str(data[point][TIME_WINDOWS_LOWER]).split(':')
            result = int(h) + (int(m) / 60)
            time_lower[point] = result

    time_upper = {}
    for point  in range(1,len(data)-1):
        if(str(data[point][TIME_WINDOWS_UPPER])!='nan'):
            h, m, s = str(data[point][TIME_WINDOWS_UPPER]).split(':')
            result = int(h) + (int(m) / 60)
            time_upper[point] = result

    return {
        'timeWindowsLower': time_lower,
        'timeWindowsUpper': time_upper
    }