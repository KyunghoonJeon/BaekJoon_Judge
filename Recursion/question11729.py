#재귀가 뭐냐: 반복되는게 있다는 것.
N=int(input())
def hanoi(x,from_pos,to_pos,aux_pos):
    if x==1:
        print(from_pos,to_pos)
        return
    hanoi(x-1,from_pos,aux_pos,to_pos)
    print(from_pos,to_pos)
    hanoi(x-1,aux_pos,to_pos,from_pos)
print(2**N-1)
hanoi(N,1,3,2)