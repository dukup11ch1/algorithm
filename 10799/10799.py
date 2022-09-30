input_pipe=input()
stack=0
pipe=0
for i in range(len(input_pipe)):
    if input_pipe[i]=='(':
        if input_pipe[i+1]==')':
            pipe+=stack
        else :
            stack+=1
            pipe+=1
    if input_pipe[i]==')':
        if input_pipe[i-1]=='(':
            pass
        else:
            stack-=1

print(pipe)
