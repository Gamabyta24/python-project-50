import argparse
def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    #parser.add_argument('-v', '--version', action='version', version='1.0')
    
    # добавляем любые другие опции
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    args = parser.parse_args()

    # Ваш основной код
    print(f'Аргумент echo: {args.echo}')

if __name__ == '__main__':
    main()