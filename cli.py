from teacher_crud import TeacherCrud

class SimpleCLI:
  def __init__(self):
    self.commands = {}

  def add_command(self, name, function):
    self.commands[name] = function

  def run(self):
    while True:
      command = input("Enter a command: ")
      if command == "quit":
        print("Goodbye!")
        break
      elif command in self.commands:
        self.commands[command]()
      else:
        print("Invalid command. Try again.")

class TeacherCLI(SimpleCLI):
  def __init__(self, teacherCRUD):
    super().__init__()
    self.teacherCRUD = teacherCRUD
    self.add_command("create", self.create)
    self.add_command("read", self.read)
    self.add_command("update", self.update)
    self.add_command("delete", self.delete)

  def create(self):
    name = input('Entre com o nome do professor: ')
    ano_nasc = input('Entre com a data de nascimento do professor: ')
    cpf = input('Entre com o CPF do professor: ')

    self.teacherCRUD.create(name, ano_nasc, cpf)

  def read(self):
    name = input("Entre com o nome do professor: ")
    self.teacherCRUD.read(name)

  def update(self):
    name = input("Entre com o nome do professor: ")
    newCpf = input("Entre com o novo CPF do professor: ")

    self.teacherCRUD.update(name, newCpf)

  def delete(self):
    name = input("Entre com o nome do professor: ")
    self.teacherCRUD.delete(name)
      
  def run(self):
    print("Bem-vindo a CLI do Professor:")
    print("Comandos disponíveis: create, read, update, delete, quit")
    super().run()