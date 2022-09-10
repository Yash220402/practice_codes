def checkBalance(p):
    stack = []
    for i in range(len(p)-1):
        if p[i]=="(" and p[i+1]==")":
            stack.insert(-1, (p[i], p[i+1]))
        
            
    if len(stack) == 0: return (True, stack)
    return (False, stack)

    
def main():
    p = "[()]{}{[()()]()}"
    p = "[(])"
    booly, stack = checkBalance(p)
    print(stack)
    
main()