a = int(input("Masukan jumlah baris (max = 26) : "))
b = int(input("Masukan jumlah shaf (max = 26)  : "))
if a > 26 :
    print("Maksimalnya 26 oy,dasar jomblo rese!")
if b > 26 :    
    print("Maksimalnya 26 oy,dasar jomblo rese!")
board = []
def lol(x):
    if x == 0:
        return "a"
    elif x == 1:
        return "b"
    elif x == 2:
        return "c"
    elif x == 3:
        return "d"    
    elif x == 4:
        return "e"    
    elif x == 5:
        return "f"    
    elif x == 6:
        return "g"    
    elif x == 7:
        return "h"    
    elif x == 8:
        return "i"
    elif x == 9:
        return "j"    
    elif x == 10:
        return "k"    
    elif x == 11:
        return "l"    
    elif x == 12:
        return "m"    
    elif x == 13:
        return "n"    
    elif x == 14:
        return "o"    
    elif x == 15:
        return "p"    
    elif x == 16:
        return "q"    
    elif x == 17:
        return "r"    
    elif x == 18:
        return "s"
    elif x == 19:
        return "t"    
    elif x == 20:
        return "u"     
    elif x == 21:
        return "v"    
    elif x == 22:
        return "w"    
    elif x == 23:
        return "x"    
    elif x == 24:
        return "y"    
    elif x == 25:
        return "z"  
    else:
        print("Noh kan jadi ERROR!")
for i in range(b):
    lal = lol(i)
    for i in range(a):
        lel = lol(i)
        e = lal + lel
        board.append(e)
def main():        
    def alp(x):
        pisan = "|"
        for i in range(a):
            atuh = board[i+x]
            lier = str(atuh)+"|"
            pisan = pisan + lier
        print(pisan)   
    alp(0)
    ruded = a
    for i in range(b-1):
        alp(ruded)
        ruded = ruded + a
main()    

    
    
