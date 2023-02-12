from string import ascii_lowercase as LOWERS


def main():
    print("=" * 50)
    print("My Program")
    print("=" * 50)

    a = [1, 2, 3]
    b = [data * 3 for data in a]
    print(b)
    myText = "Hallo world!"

    c = [text * 2 for text in myText]

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    # 어쨋거나 나열할 대상은 n, list comprehension은 큰 대상에서부터 작은 구조로 나열
    flat_arr = [n for row in arr for n in row]
    # [1,2,3,4,5,6,7,8,9,10,11,12]

    squared_list = [[n**2 for n in row] for row in arr]
    # [squared_value for row in arr]

    dict_boy = {c: n for c, n in zip(LOWERS, range(1, len(LOWERS) + 1))}


if __name__ == "__main__":
    main()
