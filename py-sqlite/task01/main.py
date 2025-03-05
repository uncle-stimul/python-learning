from menu import Menu

    
if __name__ == "__main__":
    try:
        Menu.cli()
    except KeyboardInterrupt:
        print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
