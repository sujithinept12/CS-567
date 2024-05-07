import unittest
from fitnessapp import UserProfile, Activity, DietLog, FitnessApp
import datetime

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.user = UserProfile("johndoe", 25, 75, 1.8)

    def test_bmi(self):
        expected_bmi = 75 / (1.8 ** 2)
        self.assertAlmostEqual(self.user.bmi(), expected_bmi)

    def test_update_weight(self):
        self.user.update_weight(80)
        self.assertEqual(self.user.weight, 0)

    def test_total_calories_burned(self):
        self.user.activities.append(Activity(datetime.date.today(), "Running", 30, 300))
        self.user.activities.append(Activity(datetime.date.today(), "Cycling", 45, 500))
        self.assertEqual(self.user.total_calories_burned(), 800)

    def test_total_caloric_intake(self):
        self.user.diet.append(DietLog(datetime.date.today(), "Lunch", 600))
        self.user.diet.append(DietLog(datetime.date.today(), "Dinner", 800))
        self.assertEqual(self.user.total_caloric_intake(), 1400)

    def test_recommend_daily_calories(self):
        self.assertEqual(self.user.recommend_daily_calories(), 1750.0)

    def test_record_water_intake(self):
        self.user.record_water_intake(datetime.date.today(), 500)
        self.assertEqual(len(self.user.water_intake), 1)
        self.assertEqual(self.user.water_intake[0]['amount'], 500)

    def test_set_activity_goal(self):
        self.user.set_activity_goal('steps', 10000)
        self.assertEqual(self.user.activity_goals['steps'], 10000)

class TestActivity(unittest.TestCase):
    def test_activity_str(self):
        activity = Activity(datetime.date.today(), "Walking", 60, 200)
        self.assertIn("Walking", str(activity))

class TestDietLog(unittest.TestCase):
    def test_diet_log_str(self):
        diet_log = DietLog(datetime.date.today(), "Breakfast", 500)
        self.assertIn("Breakfast", str(diet_log))

class TestFitnessApp(unittest.TestCase):
    def setUp(self):
        self.app = FitnessApp()
        self.app.add_user("johndoe", 25, 75, 1.8)

    def test_add_user(self):
        result = self.app.add_user("janedoe", 24, 65, 1.7)
        self.assertIn("added", result)
        self.assertIn("janedoe", self.app.users)

    def test_record_activity(self):
        result = self.app.record_activity("johndoe", datetime.date.today(), "Running", 30, 300)
        self.assertEqual("Activity recorded.", result)

    def test_log_diet(self):
        result = self.app.log_diet("johndoe", datetime.date.today(), "Lunch", 650)
        self.assertEqual("Diet logged.", result)

    def test_get_user_activities(self):
        self.app.record_activity("johndoe", datetime.date.today(), "Running", 30, 300)
        activities = self.app.get_user_activities("johndoe")
        self.assertIn("Running", activities[0])

    def test_get_user_diet(self):
        self.app.log_diet("johndoe", datetime.date.today(), "Lunch", 650)
        diet = self.app.get_user_diet("johndoe")
        self.assertIn("Lunch", diet[0])

    def test_get_health_tips(self):
        tips = self.app.get_health_tips("johndoe")
        self.assertIn("maintain your healthy weight", tips)

    def test_record_water_intake(self):
        result = self.app.record_water_intake("johndoe", datetime.date.today(), 500)
        self.assertEqual("Water intake recorded.", result)

    def test_record_sleep_hours(self):
        result = self.app.record_sleep_hours("johndoe", datetime.date.today(), 8)
        self.assertEqual("Sleep hours recorded.", result)

    def test_set_activity_goal(self):
        result = self.app.set_activity_goal("johndoe", "steps", 10000)
        self.assertEqual("Activity goal set.", result)

if __name__ == '__main__':
    unittest.main()
