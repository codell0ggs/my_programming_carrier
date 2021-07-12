# convert any number that is closest to a perfect number up to 50
zero = float(0)
zero5 = float(5)
ten = float(10)
ten5 = float(15)
twenty = float(20)
twenty5 = float(25)
thirty = float(30)
thirty5 = float(35)
fourty = float(40)
fourty5 = float(45)
fifty = float(50)


input_number = float(input("input number:"))

if input_number <= fifty:
    print(f"your number: {input_number}")

if input_number < zero5:
    print(f"our number: {zero}")

elif ten > input_number > zero5:
    print(f"our number: {ten}")

elif input_number < ten5:
    print(f"our number: {ten}")

elif twenty > input_number > ten5:
    print(f"our number: {twenty}")

elif input_number < twenty5:
    print(f"our number: {twenty}")

elif thirty > input_number > twenty5:
    print(f"our number: {thirty}")

elif input_number < thirty5:
    print(f"our number: {thirty}")

elif fourty > input_number > thirty5:
    print(f"our number: {fourty}")

elif input_number < fourty5:
    print(f"our number: {fourty}")

elif fifty > input_number > fourty5:
    print(f"our number: {fifty}")

elif input_number < fifty:
    print(f"our number: {fifty}")

else:
    print(f"your number is bigger than {fifty}")


