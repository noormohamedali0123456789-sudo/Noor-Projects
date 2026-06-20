def convert(Hamza):
 Hamza =Hamza.replace(":)", "🙂")
 Hamza =Hamza.replace(":(", "🙁")
 return Hamza
def main():
   user_input=input("please write what you want: " )
   print(convert(user_input))
main()
