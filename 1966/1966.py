
class Document:
    def __init__(self):
        self.docunum=0
        self.want_know=0

    def input(self):
        self.docunum,self.want_know= list(map(int, input().split(" ")))
case_num=input()
for i in range(int(case_num)):
    docu=Document()
    docu.input()
    print_queue=list(map(int, input().split(" ")))
    max_import=max(print_queue)
    print_num=0
    reselt=1
    while(1):
        if max_import==print_queue[0]:
            if docu.want_know==0:
                break
            else:
                docu.want_know-=1
            del print_queue[0]
            max_import=max(print_queue)
            reselt+=1
        else :
            if docu.want_know==0:
                docu.want_know=len(print_queue)-1
            else:
                docu.want_know-=1
            print_queue.append(print_queue[0])
            del print_queue[0]
    print(reselt)