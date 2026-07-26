import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    match = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
                  s

    )
    print(match)

    if not match:
          raise ValueError
    start_hour = int(match.group(1))


    start_minute = match.group(2)
    if start_minute is None:
           start_minute = 0
    else:
          start_minute = int(start_minute)
    start_period = match.group(3)

    end_hour =  int(match.group(4))
    end_minute = match.group(5)
    if end_minute is None:
         end_minute = 0
    else:
         end_minute = int(end_minute)
    end_period = match.group(6)
    if start_hour < 1 or  start_hour >12:
           raise ValueError
    if end_hour <1 or end_hour > 12:
           raise ValueError
    if start_period == "AM":
       if start_hour  == 12:
          start_hour = 0
    elif start_period == "PM":
     if start_hour != 12:
         start_hour += 12
    if end_period == "AM":
        if  end_hour  == 12:
             end_hour = 0
    elif end_period == "PM":
        if end_hour != 12:
             end_hour += 12
    if start_minute <0 or start_minute>59:
         raise ValueError
    if end_minute <0 or end_minute > 59:
         raise ValueError
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
if __name__ == "__main__":
     main()
