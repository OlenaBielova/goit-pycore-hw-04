import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(directory, indent=""): 
    try:
        entries = sorted(Path(directory).iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
        # print(entries)
        for entry in entries:
            if entry.is_dir():
                print(f"{indent}{Fore.BLUE} {entry.name}{Style.RESET_ALL}")
                print_directory_structure(entry, indent + "┃ ")
            else:
                print(f"{indent}{Fore.GREEN} {entry.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Доступ заборонено: {directory}{Style.RESET_ALL}")

def main():
    init(autoreset=True)  
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Використання: python3 3.py <абсолютний шлях_до_директорії>")
        return
    
    directory = Path(sys.argv[1])
    print(directory)
    if not directory.exists() or not directory.is_dir():
        print("Помилка: Вказаний шлях не є директорією або не існує.")
        return
    
    print(f"{Fore.YELLOW} {directory.name}{Style.RESET_ALL}")
    print_directory_structure(directory)

if __name__ == "__main__":
    main()

# запуск скрипта: python3 3.py /Users/elenabelova/Neoversity/python/goit-pycore-hw-04