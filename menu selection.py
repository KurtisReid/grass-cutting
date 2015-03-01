def constants(selection):
    ASCII_LOWERCASE = ("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
    ASCII_UPPERCASE = ("Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M")
    DECIMAL_DIGITS = ("0,1,2,3,4,5,6,7,8,9")
    if selection == 1:
        x = ASCII_LOWERCASE
    elif selection == 2:
        x = ASCII_UPPERCASE
    elif selection == 3:
        x = DECIMAL_DIGITS
    return x
def get_menu_options():
    print("""
Type
    1 to redisplay menu
    2 to enter location data""")
def get_location():
    try:
        title = str(input("Enter name of the file: "))
        new_file = open(title+".txt", "a")
        latitude = input("Enter your latitude data: ")
        longitude = input("Enter your longitude data: ")
        print(latitude,",",longitude, file=new_file)
        new_file.close()
    except TypeError:
        print("Type Error")
def main():
    try:
        get_menu_options()
        command_input = input("please input a command(type exit to leave) ")
        for char in command_input:
            if char in  constants(2):
                char = char.lower()
        while command_input != "exit":
            if command_input == "1":
                get_menu_options()
            if command_input == "2":
                get_location()
            command_input = input("please input a command(type exit to leave) ")
        else:
            print("program exited")
    except EOFError:
        print("EOF Error")
                
main()
