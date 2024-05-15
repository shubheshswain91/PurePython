def connect():
    raise NotImplementedError('connect() is missing code.')   # 1. Instead of pass to tell more about why the function id not implemented

#connect()


def get_users() -> dict[int, str]:             # 2. specfiy the return type makes a programmer easier to read the code
    # 3. Docstring to write documentation, install autodocstring  in VSCode
    """_summary_                 
    Retrieves the ids and usernames from a database as a dict
    Returns:
        dict[int, str]: _description_
    """
    users: dict[int, str] = {1: 'Bob', 2: 'Jeff', 3: 'Tom'}
    return users

print(get_users())

def display_users(users: dict[int, str]):
    for k,v in users.items():
        print(k, v, sep=': ')


def join_text(*strings, sep: str) -> str:   # Using *arg in function param to take as much as values we want. This is by default used in the print()
    return sep.join(strings)

def main() -> None:
    users: dict[int, str] = get_users()
    display_users(users)
    print(join_text('A', 'B', 'C', 'D', sep='-'))
    print(join_text('A', sep='-'))
    print(join_text('A', 'B', 'C', 'D', 'K', sep='*'))

if __name__ == '__main__':
    main()

