from django.test import TestCase

from .models import Task, Topic, Student, Group, Status, Answer


class TaskTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='Jane Doe')
        self.topic = Topic.objects.create(name='Etc')
        self.task = Task.objects.create(
            name='Do something',
            student=self.student,
            topic=self.topic)

    def test_create_task_without_additional_stuff(self):
        task = Task.objects.create(name='I am lazy')
        # it's usually always better to use simple 'assert X ? Y'
        self.assertTrue(task.student is None)

    def test_can_assign_and_complete_task(self):
        self.assertFalse(self.task.done)
        self.assertTrue(self.task.student.name == 'Jane Doe')
        self.task.complete()
        self.assertTrue(self.task.done)

    def test_related_tasks(self):
        self.assertTrue(self.task in self.student.tasks.all())
        self.assertTrue(self.task in self.topic.tasks.all())

    def test_simple_joins(self):
        self.assertTrue(
            self.task in Task.objects.filter(
                student__name='Jane Doe'))
        self.assertTrue(
            self.student in Student.objects.filter(
                tasks__name__in=['Do something']))


class GroupTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='Jane Doe')
        self.group = Group.objects.create(name='Everyone get in here')
        self.leader = Status.objects.create(
            leader=True, group=self.group, student=self.student)

    def test_can_include_in_group(self):
        self.assertTrue(self.student in self.group.members.all())
        self.assertTrue(self.group in
                        Group.objects.filter(members=self.student))
        self.assertTrue(self.leader in
                        Status.objects.filter(
                            student=self.student, leader=True))
        self.assertTrue(self.group in
                        Group.objects.filter(status__leader=True))


class AnswerTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='Jane Doe')
        self.task = Task.objects.create(
            name='How much is the fish',
            student=self.student)

    def test_student_can_answer(self):
        answer = Answer.objects.create(text='42',
                              student=self.student,
                              task=self.task)

        self.assertTrue(answer in self.student.answers.all())
        self.assertTrue(answer in self.task.answers.all())
