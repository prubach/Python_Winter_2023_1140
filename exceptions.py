
try:
    f = open('hello.txt', 'r')
    f_content = f.readlines()
    # A bug - my_func() doesn't exist
    f.my_func()
    print(f_content)
except FileNotFoundError as fe:
    print(fe)
# Be careful!!! This will catch all bugs in code
except Exception as e:
    print(f'Other error: {e}')
