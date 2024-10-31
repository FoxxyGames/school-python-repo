def calculate_sum(number, product):
    product *= number
    
    return product

def PrintCredits():
    print("Completed by Jasmine Matthews")

def main():
    try:
        numbers = [1, 2, 3, 4, 5, 6]
        product = 1
        for number in numbers:
            product = calculate_sum(number, product) 
        print(f'The product of the numbers is: {product}')
        
        print(f'The last number multipled was: {numbers[len(numbers)-1]}')
        PrintCredits()
    except IndexError as e:
        print(f'Run-time error: {e}')

if __name__ == '__main__':
    main()

