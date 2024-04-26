from app.services.cache_service import RedisCache
import unittest

class TestRedisCache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up method to initiate the RedisCache before tests run."""
        cls.cache = RedisCache()

    def test_set_get_delete(self):
        """Test the set, get and delete functionality of RedisCache."""
        # Test setting a value
        self.cache.set('test_key', 'Hello, Redis!')
        result = self.cache.get('test_key')
        self.assertEqual(result, 'Hello, Redis!', "Failed to set or get the value.")

        # Test deleting the key
        self.cache.delete('test_key')
        result = self.cache.get('test_key')
        self.assertIsNone(result, "Failed to delete the key.")

if __name__ == '__main__':
    unittest.main()
