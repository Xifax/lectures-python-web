from django.test import TestCase

from tasks.models import Task, Topic, Student, Group, Status


class TaskTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='Jane Doe')
        self.topic = Topic.objects.create(name='Etc')
        self.task = Task.objects.create(
                name='Do something',
                student=self.student,
                topic=self.topic)

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

