from django.db import models


class Common(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']


class Task(Common):
    description = models.TextField()
    done = models.BooleanField(default=False)

    topic = models.ForeignKey('Topic',
            on_delete=models.CASCADE,
            related_name='tasks')
    student = models.ForeignKey(
            'Student',
            on_delete=models.CASCADE,
            related_name='tasks')

    def complete(self):
        self.done = True
        self.save()
        return self


class Answer(models.Model):
    GRADES = (
        (1, 'bad'),
        (2, 'good'),
        (3, 'great')
    )
    text = models.TextField()
    grade = models.IntegerField(
        choices=GRADES,
        null=True,
        blank=True)

    student = models.ForeignKey('Student',
        related_name='answers',
        on_delete=models.CASCADE)
    task = models.ForeignKey(Task,
        related_name='answers',
        on_delete=models.CASCADE)


class Topic(Common):
    pass


class Student(Common):
    helpers = models.ManyToManyField('self', blank=True)


class Group(Common):
    members = models.ManyToManyField(
        Student,
        through='Status',
        # order is important!
        through_fields=('group', 'student'),
    )


class Status(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    leader = models.BooleanField(default=False)
