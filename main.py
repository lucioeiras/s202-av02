from config.database import Database
from teacher_crud import TeacherCrud
from cli import TeacherCLI

db = Database("bolt://18.215.14.216:7687", "neo4j", "title-date-boats")

teacher = TeacherCrud(db)

teacher.create('Chris Lima', 1956, '189.052.396-66')

print('Pesquisando Chris Lima:')
teacher.read('Chris Lima')

teacher.update('Chris Lima', '162.052.777-77')

teacherCLI = TeacherCLI(teacher)
teacherCLI.run()
