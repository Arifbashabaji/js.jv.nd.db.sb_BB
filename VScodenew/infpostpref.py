from collections import deque
stack=deque()
def main()->None:
    inpstr=input("Enter the infix postfix or prefix expression:")
    print("Enter the eq option:")
    print("1:post->pref\n2:post->infi\n3:pref->post\n4:pref->infi\n5:infi->post\n6:infi->pref\n")
    while True:
        try:
            chc=int(input("OP:-"))
            if chc>6:
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter a valid integer in range")
def postToPref(inpstr:str)->str:
    str


if __name__=='__main__':
    main()
