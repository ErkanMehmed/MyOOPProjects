from unittest import TestCase, main
from datetime import datetime
from personal_finance_manager.goal import Goal


class GoalTest(TestCase):
    def setUp(self):
        self.goal = Goal("Target", 20)

    def test_init(self):
        self.assertEqual("Target", self.goal.target_name)
        self.assertEqual(20, self.goal.target_amount)
        self.assertEqual(0.0, self.goal.current_amount)
        now = datetime.now()
        self.assertEqual(now.month, self.goal.month)
        self.assertEqual(now.year, self.goal.year)

    def test_target_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.goal.target_name = 23
        self.assertEqual("Goal name must be a non-empty string", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.goal.target_name = ''
        self.assertEqual("Goal name must be a non-empty string", str(ex.exception))

    def test_target_amount_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.goal.target_amount = 0
        self.assertEqual("Target amount must be greater than 0", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.goal.target_amount = -1
        self.assertEqual("Target amount must be greater than 0", str(ex.exception))

    def test_add_savings_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.goal.add_savings(0)
        self.assertEqual("Amount to save must be greater than 0", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.goal.add_savings(-1)
        self.assertEqual("Amount to save must be greater than 0", str(ex.exception))

    def test_add_savings(self):
        result = self.goal.add_savings(3)
        self.assertEqual(3.0, self.goal.current_amount)
        self.assertEqual("The funds 3лв. have been allocated for Target.", result)

    def test_is_not_achieved(self):
        result = self.goal.is_achieved()
        self.assertFalse(result)

    def test_is_achieved(self):
        self.goal.current_amount = 30
        result = self.goal.is_achieved()
        self.assertTrue(result)

    def test_get_progress_percentage(self):
        result = self.goal.get_progress_percentage()
        self.assertEqual(0, result)

if __name__ == '__main__':
    main()