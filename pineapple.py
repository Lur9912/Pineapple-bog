import webbrowser

def main():
  password = input("Введите пароль: ")
  if password == "redddos": 
    while True:
      choice = input("\033[91m1. Перейти к софту\033[0m\n\033[94m2. Выход\033[0m\nВыберите опцию: ") 
      if choice == '1':
        webbrowser.open_new_tab("https://redstresser.org")
      elif choice == '2':
        print("ну и пошел нахуй!!!")
        break
      else:
        print("Неверный ввод. Пожалуйста, выберите 1 или 2.")
  else:
    print("Неверный пароль!")

if __name__ == "__main__":
  main()