"""Смоделируйте прием успешно окончивших тренинг студентов на работу в EPAM.
Вам необходимо будет реализовать класс Student, будущие создаваемые объекты которого описываются именем, 
фамилией, возрастом и набором навыков. Говоря о навыках, считается, что все без исключения студенты 
знают английский язык.Также реализуйте в классе следующие методы: 
-зачисление на курс (в результате работы которого у объекта-студента 
изменяется логический атрибут is_learning на значение True; метод вызывается автоматически при создании объекта);
-обучение (в результате работы которого студенты помимо английского языка, смогут пополнить свой багаж знаний еще такими навыками, 
как SQL, Linux и Python);
-прием на работу (отрабатывает успешно, если студент обладает всеми необходимыми навыками).
Создайте трех разных студентов. Двоих студентов обучите всем навыкам. Третий, к всеобщему сожалению, 
не выучит Python. Попробуйте принять всех троих на работу."""


class Student:
    """The class represents EPAM student who study to get job invitaion"""
    required_skills = ('English', 'SQL', 'Linux', 'Python')

    def __init__(self, name: str, second_name: str, age: int, *skills) -> None:
        """Creates the Student with name,second name and age. 
        Skills should be added as additional parameters"""
        self.name = name
        self.second_name = second_name
        self.age = age
        self.is_learning = False
        self.is_working = False
        self.skills = set(skills)
        self.skills.add("English")
        self.accept_learn()

    def accept_learn(self):
        """Method accepts student to EPAM Lab"""
        self.is_learning = True

    def accept_job(self):
        """Method checks if a student will be hired or not, last call of this method saves result in self.is_working"""
        for req_skill in self.required_skills:
            if req_skill not in self.skills:
                return False
        self.is_working = True
        return True

    def train_skill(self, skill_name: str):
        """Method takes name of skill. If skill name not in the skills list, it offers to add new one."""
        if skill_name in self.skills:
            print(f"{self.name} already knows {skill_name}")
        elif skill_name in self.required_skills:
            self.skills.add(skill_name)
        else:
            print('Skill name not found in skills names. If you want to add this skill as new, type "yes", if not, type any', end=' ')
            if input() == 'yes':
                self.skills.add(skill_name)


if __name__ == '__main__':
    st1 = Student('Bob', 'Smith', '20', 'English', 'French', 'Python')
    st2 = Student('John', 'McKinsey', '28', 'English', 'Linux')
    st3 = Student('Rob', 'Kendal', '18', 'English')
    # Study process
    # Student 1 study
    st1.train_skill('English')
    st1.train_skill('SQL')
    st1.train_skill('Linux')
    # Student 2 study
    st2.train_skill('SQL')
    st2.train_skill('Linux')
    st2.train_skill('Python')
    # Student 3 study
    st3.train_skill('SQL')
    st3.train_skill('Linux')

    # Check students for job requirement
    studs = [st1, st2, st3]
    for stud in studs:
        print('{0} {1} is hired: {2}'.format(stud.name, stud.second_name, stud.accept_job()))
