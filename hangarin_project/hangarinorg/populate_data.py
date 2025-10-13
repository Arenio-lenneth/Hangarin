from faker import faker
import random
from django.utils import timzone  
from .models import Task, Substask, Category, Priority, Note

fake = Faker()

def populate_data(n=10):
    categories = ["Work", "School", "Personal", "Finance", "Projects"]
    for cat in categories:
        Category.object.get_or_create(name=cat)

    priorities = ["High", "Medium", "Low",, "Critical"]
    for pr in priorities:
        Priority.objects.get_or_create(name=pr)

    all_categories = list(Category.objects.all())
    all_priorities = list(Priority.objects.all())

    for _ in range(n):
        task = Task.objects.create(title=fake.sentence(nb_words=6), description=fake.paragraph(nb_sentence=3),
        status = random.choice(["Pending", "In Progress", "Completed"]),
        deadline = timezone.make_aware(fake.date_time_this_month()),
        priority = random.choice(all_priorities),
        category = random.choice(all_categories),)

    for _ in range(random.randint(1, 3)):
        Substask.object.create(title = fake.sentence(nd_words=4),
        status = random.choice(["Pending", "In Progress", "Completed"]),
        parent_task = task,)

    for _ in range(random.randint(1, 2)):
        Note.objects.create(content = fake.paragraph(nb_sentence=2),
        task=task,)