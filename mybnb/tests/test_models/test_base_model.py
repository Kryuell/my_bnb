#!/usr/bin/python3
"""Defines unittests for models/base_model.py. """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def test_id(self):
        """Test id is a string of a valid UUID."""
        m = BaseModel()
        self.assertIsInstance(m.id, str)
        self.assertEqual(uuid.UUID(m.id).version, 4)

    def test_datetime(self):
        """Test created_at and updated_at are datetime objects."""
        m = BaseModel()
        self.assertIsInstance(m.created_at, datetime)
        self.assertIsInstance(m.updated_at, datetime)

    def test_str(self):
        """Test __str__ method."""
        m = BaseModel()
        expected = f"[BaseModel] ({m.id}) {m.__dict__}"
        self.assertEqual(str(m), expected)

    def test_save(self):
        """Test save method updates updated_at."""
        m = BaseModel()
        old_updated = m.updated_at
        m.save()
        self.assertNotEqual(old_updated, m.updated_at)
        self.assertGreater(m.updated_at, old_updated)

    def test_to_dict(self):
        """Test to_dict method."""
        m = BaseModel()
        m_dict = m.to_dict()

        self.assertEqual(m_dict['__class__'], 'BaseModel')
        self.assertEqual(m_dict['id'], m.id)
        self.assertEqual(m_dict['created_at'], m.created_at.isoformat())
        self.assertEqual(m_dict['updated_at'], m.updated_at.isoformat())
        self.assertIsInstance(m_dict['created_at'], str)
        self.assertIsInstance(m_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()