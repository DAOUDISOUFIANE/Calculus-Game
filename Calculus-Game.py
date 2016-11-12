import random
def operation():
    k=0
    u=0
    n=0
    y=0
    j=0
    for i in range(0,4):
        level = 1
        if(level == 1):
            print("level 1    requirement : mental calculation / difficulty : Easy");
            for i in range(0,10):
                a = random.randint(0,33)
                b = random.randint(0,33)
                d = int(input(str(a)+" + "+str(b)+" = "))
                if d == a+b :
                    j +=1
                    k +=1
                else:
                    print("INCORRECT!  the right answer is ",a+b);
            if(k <8):
                print("------- GAME OVER -------");
                average1 = (k*10)
                print(" your average score is "+str(average1)+"%    you are a begineer!");
                break
            else:     
                level = level +1
        if(level == 2):
            print("level 2  requirement : mental calculation  difficulty : Normal");
            for i in range(0,10):
                a = random.randint(0,70)
                b = random.randint(0,70)
                op = random.randint(0,1)
                if(op == 0):
                    d = int(input(str(a)+" + "+str(b)+" = "))
                    if d == a+b :
                        j +=1
                        u +=1
                    else:
                        print("INCORRECT!  the right answer is ",a+b);
            
                elif(op == 1):
                        d = int(input(str(a)+" - "+str(b)+" = "))
                        if d == a-b :
                            j +=1
                            u +=1
                        else:
                            print("INCORRECT!  the right answer is ",a-b);
            if(u<8):
                print("------- GAME OVER -------");
                average2 = (u*10)
                totalaverage = (u + k)*5
                print(" your total average score is "+str(totalaverage)+"%   you are an intermediate!");
                break
            else:    
                level = level+1
        if(level == 3):
            print("level 3    requirement : use a paper to solve  difficulty : Hard  ");
            for i in range(0,10):
                a = random.randint(0,99)
                b = random.randint(0,99)
                c = random.randint(0,33)
                op = random.randint(0,3)
                if(op == 0):
                    d = int(input(str(a)+" + "+str(b)+" = "))
                    if d == a+b :
                        j +=1
                        n +=1
                    else:
                        print("INCORRECT!  the right answer is ",a+b);
            
                elif(op == 1):
                        d = int(input(str(a)+" * "+str(b)+" = "))
                        if d == a*b :
                            j +=1
                            n +=1
                        else:
                            print("INCORRECT!  the right answer is ",a*b);
                elif(op ==2):
                        d = int(input(str(a)+" - "+str(b)+" = "))
                        if d == a-b :
                            j +=1
                            n +=1
                        else:
                            print("INCORRECT!  the right answer is ",a-b);
                else:
                    b = b + 1
                    a = a*b
                    d = int(input(str(a)+" / "+str(b)+" = "))
                    if d == a/b :
                        j +=1
                        n +=1
            if(n<8):
                print("------- GAME OVER -------");
                average3 = (n*10)
                totalaverage2 = (n + u + k)*(10/3)
                print(" your total average score is "+str(totalaverage2)+"%   you have an advanced level!");
                break
            else:
                level = level+1
        if(level == 4):
            print("level 4    requirement : use a paper to solve   difficulty : Hero ");
            for i in range(0,10):
                a = random.randint(0,99)
                b = random.randint(0,99)
                c = random.randint(0,99)
                op = random.randint(0,3)
                if(op == 0):
                    d = int(input(str(a)+" + "+str(b)+" = "))
                    if d == a+b :
                        j +=1
                        y +=1
                    else:
                        print("INCORRECT!  the right answer is ",a+b);
            
                elif(op == 1):
                        d = int(input(str(a)+" * "+str(b)+" = "))
                        if d == a*b :
                            j +=1
                            y +=1
                        else:
                            print("INCORRECT!  the right answer is ",a*b);
                elif(op ==2):
                        d = int(input(str(a)+" - "+str(b)+" = "))
                        if d == a-b :
                            j +=1
                            y +=1
                        else:
                            print("INCORRECT!  the right answer is ",a-b);
                else:
                    b = b + 1
                    a = a*b
                    d = int(input(str(a)+" / "+str(b)+" = "))
                    if d == a/b :
                        j +=1
                        y +=1
            if(y<8):
                print("------- GAME OVER -------");
                average4 = (y*10)
                totalaverage2 = (n + u + k + y)*(5/2)
                print(" your total average score is "+str(totalaverage2)+"%   you have an advanced level!");
                break
            else:
                average4 = (y*10)
                totalaverage2 = (n + u + k + y)*(5/2)
                print("------- CONGRATULATION YOU WON -------");
                print(" your total average score is "+str(totalaverage2)+"%   you are the God of Mathematics!");
                break
##################################################################################################################################################################################################
operation()
