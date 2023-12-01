print("\t\t\t*** Welcome to the CipherSecret ***\n")



option = int(input("Would you like to encode(press 1) or decode(press 2) or would you like to access History(press 3)?"))


match option:
    case 1:
        import random
        message = input("\nEnter the message which you wanna encode:\n\t")  
        # message = "Hi Huzaifa! how are you I am going to visit you tomorrow for a while Hope you will help me."
        # f.write(message)
        a = message.split(" ")
        random_let = ['abc', 'def', 'ghi', 'jkl', 'pqk', 'mno', 'pqp', 'rst', 'uvw', 'xyz',"lmn", "opq", "ruv", "wxy", "zab", "cde", "fgh", "ijk"]
        new_msg = []
        for i in a:
            i = list(i)
            if len(i)>=3:
                f_l = []
                f_l.append(i[0])
                i=i[1:] 
                i.append(f_l[0]) 
                i = list(random_let[random.randint(0, len(random_let)-1)]) + i + list(random_let[random.randint(0, len(random_let)-1)])
                f_l=[]
                i=''.join(i)
                new_msg.append(i)
                # print(i)
            else:
                i = (i[::-1])
                i=''.join(i)
                new_msg.append(i)
            
        final_msg = ' '.join(new_msg)

        print(f"\nThe encoded message is :\n\t {final_msg}")
    case 2:
        message = input("\nEnter the message which you wanna decode :\n\t")
        # message = "iH pqpuzaifaHijk fghowhmno cdereaijk lmnouylmn I ma ruvoinggwxy ot zabisitvfgh ghiouyopq uvwomorrowtabc ruvorfabc a fghhilewlmn zabopeHzab defouypqk rstillwijk wxyelphijk em"
        a = message.split(" ")
        new_msg = []

        for i in a :           
            if len(i) <= 3:             
                i = (i[::-1])      # To simply reverse a string
                n=''.join(i)       # n will contain a single string that represents the concatenation of all the elements in the list i.
                new_msg.append(n) # If block is all done
            else:
                i = i[3:-3]         # Removes three letters from start and end.
                l = i[-1]           # To store the last letter 
                alt_i = i[:-1]      # To remove the last letter
                final_i = l + alt_i
                new_msg.append(final_i)

        final_msg = ' '.join(new_msg)

        print(f"\nThe decoded message is :\n\t{final_msg}")
    # case 3:
        
    case _:
        print("Plz follow the instructions!")



print("\n\t\t\t*** Thanks for using CipherSecret ***")