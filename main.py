# python3

def parallel_processing(n, m, data):
    output = []
    counter=[0]*n
    number=0
    i=0
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    singles=(m+n-1)//n
    while singles>0:
        index=i%n
        output.append((index,counter[index]))
        counter[index]+=data[number]
        number+=1
        i+=1
        if number>=m:
            break
        if index==n-1:
            singles-=1
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n=list(map(int,input().split()))
    m=list(map(int,input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data=list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line 
    for i, j in result:
        print(i,j)

if __name__ == "__main__":
    main()
