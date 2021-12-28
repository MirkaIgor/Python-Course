"""Смоделируйте прием успешно окончивших тренинг студентов на работу в EPAM.
Вам необходимо будет реализовать класс Student, будущие создаваемые объекты которого описываются именем, фамилией, возрастом и набором навыков. Говоря о навыках, считается, что все без исключения студенты знают английский язык.
Также реализуйте в классе следующие методы: 
-зачисление на курс (в результате работы которого у объекта-студента изменяется логический атрибут is_learning на значение True;
метод вызывается автоматически при создании объекта);
-обучение (в результате работы которого студенты помимо английского языка, смогут пополнить свой багаж знаний еще такими навыками, 
как SQL, Linux и Python);
-прием на работу (отрабатывает успешно, если студент обладает всеми необходимыми навыками).
Создайте трех разных студентов. Двоих студентов обучите всем навыкам. Третий, к всеобщему сожалению, 
не выучит Python. Попробуйте принять всех троих на работу."""

class Student:
    skill_list = ['English','SQL','Linux','Python']
    _min_grade_for_gob = 4 #Минимальная оценка знаний по всем предметам для приема на работу

    def __init__(self,name :str,second_name: str,age: int,skills=None) -> None:
        """Creates the Student with name,second name and age. 
        Skills parameter should be a dictionary containing name of skills as keys (default: English,SQL,Linux,Python) and
        grades 0-5 for each skill as dict value. for example: {'English':4,'SQL':3,'Linux':2,'Python':5}"""
        self.name = name
        self.second_name = second_name
        self.age = age
        #Следующие 6 строк обрабатывают навыки студента. Если в аргумент не переданы навыки, то всем нужным навыкам присваиваем ноль.
        #Если нужные навыки переданы не полностью, то их принимаем, а остальным неизвестным присваиваем ноль
        #Помимо нужных для приема на работу навыков из поля skill_list, студент может иметь прочие навыки (например French, C++,Java и тп),
        #для приема на работу играют роль все равно только нужные, но прочие тоже запишем студенту
        if not skills:
            self.skills = {skill_name:0 for skill_name in self.skill_list}
        else:
            self.skills = {skill_name:skills[skill_name] for skill_name in skills.keys()}
            keys_diff = set(self.skill_list)^set(self.skills.keys())
            if keys_diff:
                self.skills.update({skill_name:0 for skill_name in keys_diff})
        self.accept_learn()

    def accept_learn(self):
        self.is_learning = True

    def accept_job(self):
        """Method checks if a student will be hired or not, last call of this method saves result in self.is_working"""
        self.skill_list = set([True if self.skills[skill]>=self._min_grade_for_gob else False for skill in self.skill_list ])
        if self.skill_list == {True}:
            self.is_working =True
            return True
        else:
            self.is_working = False
            return False


    def train_skill(self,skill_name:str):
        """Method takes name of skill. If skill name not in the skills list, it offers to add new one."""
        if skill_name in self.skills.keys():
            self.skills[skill_name]+=1
        else:
            print('Skill name not found in skills names. If you want to add this skill as new, type "yes", if not, type any',end=' ')
            if input() == 'yes':
                self.skills[skill_name]=1

if __name__ == '__main__':
    st1 = Student('Bob','Smith','20',{'English':3,'SQL':1,'Linux':0,'Python':4})
    st2 = Student('John','McKinsey','28',{'English':5,'Python':4})
    st3 = Student('Rob','Kendal','18')
    #Study process
    #Student 1 study
    st1.train_skill('English')
    st1.train_skill('English')
    st1.train_skill('SQL')
    st1.train_skill('SQL')
    st1.train_skill('SQL')
    st1.train_skill('Linux')
    st1.train_skill('Linux')
    st1.train_skill('Linux')
    st1.train_skill('Linux')
    #Student 2 study
    st2.train_skill('SQL')
    st2.train_skill('SQL')
    st2.train_skill('SQL')
    st2.train_skill('SQL')
    st2.train_skill('Linux')
    st2.train_skill('Linux')
    st2.train_skill('Linux')
    st2.train_skill('Linux')
    #Student 3 study
    st3.train_skill('English')
    st3.train_skill('English')
    st3.train_skill('English')
    st3.train_skill('English')
    st3.train_skill('English')
    st3.train_skill('SQL')
    st3.train_skill('SQL')
    st3.train_skill('SQL')
    st3.train_skill('SQL')
    st3.train_skill('Linux')
    st3.train_skill('Linux')
    st3.train_skill('Linux')
    st3.train_skill('Linux')
    st3.train_skill('Python')
    st3.train_skill('Python')
    #Check students for job requirement
    studs = [st1,st2,st3]
    for i in range(3):
        print('{0} {1} is hired: {2}'.format(studs[i].name,studs[i].second_name,studs[i].accept_job()))

    

