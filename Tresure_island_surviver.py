print("Welcome to Treasure Island.\nYour mission is to find the treasure")
ans=input("Left or Right?")
if ans=="Left":
    ans2=input("swim or wait?")
    if ans2=="wait":
        ans3=input("which door red,yellow,blue?")
        if ans3=="red":
            print("Looser burnt by fire")
        elif ans3=="blue":
            print("Looser eaten by lobster")
        else:
            print("!!!!!!!! you win !!!!!!!!")
    elif ans2=="swim":
        print("Big looser")
    
elif ans=="Right":
    print("Looser")
