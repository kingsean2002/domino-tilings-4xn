##############################
# NAME: SEAN GAROFAL-HEAVNER #
# DATE: 04/10/22             #
# DISTINCT DOMINO TILINGS    #
##############################


def d(n):
    A = [0] * (n + 1)
    A[0] = 1
    A[1] = 0
    dp = 0

    for i in range(2, n+1):
        ## reccurence relation equation for 4xn dominoe grid
        A[i] = A[i - 1] + 5 * A[i - 2] + A[i - 3]- A[i - 4]
        dp = A[i] + A[i - 1]
    return dp

n = int(input("Enter Designated Amount of Datasets (1-1000): "))
w = []

if n > 1000 or n < 1 or type(n) != int:
    print('Please Enter A Valid Input')
    n = int(input("Enter Designated Amount of Datasets (1-1000): "))
else:
    for i in range(n):
        width = int(input("Enter Grid Width: "))
        if width <= 23:  # 32 BIT WIDTH CONSTRAINT
            w.append(width)
        else:
            print("Input will exceed 32 BIT threshold")
            width = int(input("Enter Grid Width(0 to 23): "))

w = sorted(w)
count = 0

while count != n:
    x = d(w[count])
    count += 1
    print(f'{count} {x}')
