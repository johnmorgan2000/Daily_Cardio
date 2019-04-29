def main():
    bill = [9.50, 11.75, 18.50, 3, 3]
    allergy_index = 0
    money_given = 30

    # bill = [1]
    # allergy_index = 0
    # money_given = 1
    solution2(bill, allergy_index, money_given)

def solution1(bill, allergy_index, money_given):
    shared_price= 0
    for price in bill:
        shared_price += price
    shared_price -= bill[allergy_index]
    cut = shared_price / 2
    diff = money_given - cut
    print(diff)

def solution2(bill, allergy_index, money_given):
    shared_price= 0
    index = 0
    while index < len(bill):
        shared_price += bill[index]
        index += 1
    shared_price -= bill[allergy_index]
    cut = shared_price / 2
    diff = money_given - cut
    print(diff)

if __name__ == "__main__":
    main()
