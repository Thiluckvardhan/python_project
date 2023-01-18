rangenumber=input("Enter a Nth Number: ")
if rangenumber.isdigit():
    rangenumber=int(rangenumber)
    count = 0
    latest = 0
    num = 1
    while True:
        num2 = 0
        num1 = num
        factors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factors += 1
            if factors>=3:
                continue
        if factors == 2:#checking prime or not
            while num1 != 0:
                rem = num1 % 10
                num1 //= 10
                num2 = num2 * 10 + rem
        if num == num2:#checking palindrome or not
            count += 1
            latest = num

        num = num + 1
        if count==rangenumber:
            break
    print(rangenumber, "th Prime Pallindrome Number is ", latest)
else:
    print("Please input a Number")