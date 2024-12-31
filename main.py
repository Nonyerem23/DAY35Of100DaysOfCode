import os
import time

todolist = []
def printlist():
  print()
  for item in todolist:
    print(item)
  print()
while True:
  print()
  menu = input("\033[32mToDo List Manager😎😎😎\n\033[0m Do you want to view, add, edit, remove or delete the todo list?\n")

  if menu=="view":
    printlist()
  elif menu=="add":
    item = input("What do you want to add?\n")
    todolist.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n")
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="yes":
      if item in todolist:
        todolist.remove(item)
  elif menu=="edit":
    item = input("What do you want to edit?\n")
    
    new = input("What do you want to change it to?\n")
    for i in range(0,len(todolist)):
      if todolist[i]==item:
        todolist[i]=new
  elif menu=="delete":
    todolist = []
  time.sleep(1)
  os.system('clear')


