from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
    def test_todo_creation(self):
        todo = Todo.objects.create(
            task="Test Task",
            description="Test Description",
            is_completed=False
        )
        self.assertEqual(todo.task, "Test Task")
        self.assertEqual(todo.description, "Test Description")
        self.assertFalse(todo.is_completed)
        self.assertTrue(todo.created)  # Check created timestamp is set
        self.assertEqual(str(todo), "Test Task")  # Test __str__ method