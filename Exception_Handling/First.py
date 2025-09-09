def read_file(filename):
    try:
        with open(filename,'r') as file:
            return file.read()
    
    except FileNotFoundError:
        print('File not found')

    except PermissionError:
        print('Permission denied')

    
