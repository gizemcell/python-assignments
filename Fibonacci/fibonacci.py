import sys


#calculation fibbonacci by using naive approach
def naive(x,file):
    if x == 1 or x == 2:
        file.write("\nfib({})".format(x)+" = 1")
        return 1
    else:
        file.write("\nfib({})".format(x)+" = "+"fib({}) + fib({})".format(x-1,x-2))
        return naive(x - 1,file) + naive(x - 2,file)


def writing_naive(output_naive,input_file):
    output_naive.write(32 * "-")
    for line in input_file:
        item = line.split()[0]
        output_naive.write("\n")
        output_naive.write("Calculating %s. Fibonacci number:" % item)
        if int(item)<1:
            output_naive.write("\nERROR: Fibonacci cannot be calculated for the non-positive numbers!")
            output_naive.write("\n%s. Fibonacci number is: nan" % (item))
            output_naive.write("\n"+32 * "-")
        else:
            result = naive(int(item), output_naive)
            output_naive.write("\n%s. Fibonacci number is: %d" % (item, result))
            output_naive.write("\n" + 32 * "-")

#calculation fibbonacci by using eager approach
def eager(x,file,list,list2):
    if x in list:
        calculated=list2[list.index(x)]
        file.write("\nfib({}) = {}".format(x,calculated))
        return calculated
    elif x == 1 or x == 2:
        file.write("\nfib({}) = 1".format(x))
        list.append(x)
        list2.append(1)
        return 1
    else:
        file.write("\nfib({}) = fib({}) + fib({})".format(x,x-1,x-2))
        calculation=eager(x-1, file, list, list2) + eager(x-2, file, list, list2)
        list.append(x)
        list2.append(calculation)
        return calculation

#writing results to the output file
def writing_eager(output_eager,input_file):
    output_eager.write(32 * "-")
    list=[] #it is used for to store order numbers of calculated elements of fibonacci such as 2th fibo will be stored
    list2=[] #it is used for to store results of calculated elements of fibonacci
             # such as result of 2th element of fibo is 1 will be stored
    for line in input_file:
        item = line.split()[0]
        output_eager.write("\n")
        output_eager.write("Calculating %s. Fibonacci number:" % item)
        if int(item)<1:
            output_eager.write("\nERROR: Fibonacci cannot be calculated for the non-positive numbers!")
            output_eager.write("\n%s. Fibonacci number is: nan" % (item))
            output_eager.write("\n"+32 * "-")
        else:
            result = eager(int(item), output_eager,list,list2)
            output_eager.write("\n%s. Fibonacci number is: %d" % (item, result))
            output_eager.write("\n" + 32 * "-")
    output_eager.write("\nStructure for the eager solution:\n"+"{}".format(sorted(list2)))
    output_eager.write("\n"+32 * "-")



def main():
    input_file=open(sys.argv[1],"r")
    output_naive=open(sys.argv[2],"w")
    output_eager = open(sys.argv[3], "w")
    writing_naive(output_naive,input_file)
    input_file.close()
    input_file = open(sys.argv[1], "r")
    writing_eager(output_eager,input_file)
    input_file.close()
    output_eager.flush()
    output_eager.close()
    output_naive.flush()
    output_naive.close()








if __name__=="__main__":
    main()