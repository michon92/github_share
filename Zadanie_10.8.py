def file_open_program(filename):
    """Open txts files"""
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
            print(f"\nFile: {filename} :")
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"\nFile {filename} doesn't exist")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    file_open_program(filename)


