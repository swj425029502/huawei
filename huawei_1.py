

def extend(new,li,k):
    new.extend(li[:k])
    for i in range(k):
        if li:
            li.pop(0)

def process(new,li,k):
    epoch=len(li)//k
    if epoch>0:
        for i in range(epoch):
            extend(new, li, k)
            epoch-=1
    if epoch<0:
        new_yu = len(li) % k
        extend(new,li,new_yu)


if __name__ == '__main__':

    li_1 = [1, 7, 4, 3, 4]
    li_2 = [2, 5, 6, 7, 9, 5, 7]
    k = 3
    # k=int(input())
    # li_1=input().strip()
    # li_2=input().strip()

    li_3=[]

    length=min(len(li_1),len(li_2))

    epoch=length//k
    yu=length%k

    i=0
    while i<=epoch:
        extend(li_3,li_1,k)
        extend(li_3,li_2,k)
        i+=1

    new_len_1=len(li_1)
    new_len_2=len(li_2)


    if new_len_1>new_len_2:
        extend(li_3,li_1,k)
        extend(li_3,li_2,yu)
        process(li_3,li_1,k)

    elif new_len_1==new_len_2:
        extend(li_3,li_1,yu)
        extend(li_3,li_2,yu)
    else:
        extend(li_3,li_1,yu)
        extend(li_3,li_2,k)
        process(li_3,li_2,k)

    print(li_3)