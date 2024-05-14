from collections import deque
queue = deque()

def check():
    for i in input("입력 : "):
        queue.append(i)
    
    for _ in range(int(len(queue)/2)):
        if queue.popleft() == queue.pop():
            pass
        else:
            print("회문 X")
            return False
    print("회문")
    return True

check()
 