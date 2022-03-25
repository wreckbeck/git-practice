def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    #This is Yonese's code change
    max_numbers = numbers[0]
    for num in numbers:
        if num > max_number:
            max_num = num 
    return max



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
