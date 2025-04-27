def Readfile(filename):
    try:
        file = open(filename, 'r')
        Reading = file.readlines()
        a = len(Reading)
        for i in range(0, a):
            print(f"Line {i + 1} = {Reading[i]}", end='')

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

Readfile("sample.txt")