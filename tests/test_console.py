#!/usr/bin/python3
"""
Test cases for the HBNBCommand class.
"""

import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNBCommand class.
    """

    def test_module_docs(self):
        """
        Test if the module has documentation.
        """
        module_doc = __import__("console").__doc__
        self.assertGreater(len(module_doc), 0)

    def test_class_docs(self):
        """
        Test if the class has documentation.
        """
        class_doc = __import__("console").HBNBCommand.__doc__
        self.assertGreater(len(class_doc), 0)

    def test_quit(self):
        """
        Test 'quit' command.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual("", f.getvalue().strip())

    def test_EOF(self):
        """
        Test 'EOF' command.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual("", f.getvalue().strip())

    def test_create(self):
        """
        Test 'create' command.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertEqual(36, len(f.getvalue().strip()))

    def test_create_no_class_name(self):
        """
        Test 'create' command with no class name.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_create_invalid_class_name(self):
        """
        Test 'create' command with invalid class name.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_no_class_name(self):
        """
        Test 'show' command with no class name.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_show_invalid_class_name(self):
        """
        Test 'show' command with invalid class name.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_no_instance_id(self):
        """
        Test 'show' command with no instance id.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_show_instance_not_found(self):
        """
        Test 'show' command with instance not found.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_destroy_no_class_name(self):
        """
        Test 'destroy' command with no class name.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_destroy_invalid_class_name(self):
        """
        Test 'destroy' command with invalid class name.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_destroy_no_instance_id(self):
        """
        Test 'destroy' command with no instance id.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_destroy_instance_not_found(self):
        """
        Test 'destroy' command with instance not found.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertEqual("** no instance found **", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
