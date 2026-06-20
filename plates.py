def main():
    plate  = input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print ("Invalid")
def is_valid(s):
     if len(s) < 2  or   len(s) > 6:
         return False
     if not s[0].isalpha() or not s[1].isalpha():
         return False

     if not s.isalnum():

         return False


     found_number = False

     for char in s:
         if char.isdigit():
            if char == "0" and not found_number:
                return False
            found_number = True
         elif found_number:
                return False
     return True
main()


