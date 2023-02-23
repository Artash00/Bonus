import time

try:
    inputTime = input("Insert time to count down (h:m:s) ")
    sep = inputTime.split(":")
    h = int(sep[0])
    m = int(sep[1])
    s = int(sep[2])
    while h >= 0:
        while m >= 0:
            while s >= 0:
                if h <= 9:
                    print("0", h, ":", sep = "", end = "")
                else:
                    print(h, ":", sep = "", end = "")
                if m <= 9:
                    print("0", m, ":", sep = "", end = "")
                else:
                    print(m, ":", sep = "", end = "")
                if s <= 9:
                    print("0", s, sep = "")
                else:
                    print(s, sep = "")
                time.sleep(1)
                s -= 1
            m -= 1
            s = 59
        h -= 1
        m = 59
except:
    print ("Please enter numbers and follow the form (h:m:s)")
