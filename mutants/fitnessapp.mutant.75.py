import datetime

class UserProfile:
    def __init__(self, username, age, weight, height):
        self.username = username
        self.age = age
        self.weight = weight  # in kilograms
        self.height = height  # in meters
        self.activities = []
        self.diet = []
        self.water_intake = []
        self.sleep_hours = []
        self.activity_goals = {'steps': 0, 'active_minutes': 0}

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_height(self, new_height):
        self.height = new_height

    def bmi(self):
        return self.weight / (self.height ** 2)

    def update_age(self, new_age):
        self.age = new_age

    def delete_profile(self):
        del self

    def total_calories_burned(self):
        return sum(activity.calories_burned for activity in self.activities)

    def total_caloric_intake(self):
        return sum(diet.calories for diet in self.diet)

    def recommend_daily_calories(self):
        bmr = 10 * self.weight + 1.25 * (self.height * 100) - 5 * self.age
        if self.activities:
            activity_factor = 1.2  # Assuming light activity level
            return bmr * activity_factor
        else:
            return bmr

    def record_water_intake(self, date, amount):
        self.water_intake.append({'date': date, 'amount': amount})

    def record_sleep_hours(self, date, hours):
        self.sleep_hours.append({'date': date, 'hours': hours})

    def set_activity_goal(self, activity_type, goal):
        self.activity_goals[activity_type] = goal

class Activity:
    def __init__(self, date, activity_type, duration, calories_burned):
        self.date = date
        self.activity_type = activity_type
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.activity_type}, {self.duration} minutes, {self.calories_burned} kcal burned"

class DietLog:
    def __init__(self, date, meal, calories):
        self.date = date
        self.meal = meal  # e.g., 'Breakfast', 'Lunch', 'Dinner', 'Snack'
        self.calories = calories

    def __str__(self):
        return f"{self.date}: {self.meal}, {self.calories} kcal"

class FitnessApp:
    def __init__(self):
        self.users = {}

    def add_user(self, username, age, weight, height):
        if username not in self.users:
            self.users[username] = UserProfile(username, age, weight, height)
            return f"User {username} added."
        return "User already exists."

    def record_activity(self, username, date, activity_type, duration, calories_burned):
        if username in self.users:
            activity = Activity(date, activity_type, duration, calories_burned)
            self.users[username].activities.append(activity)
            return "Activity recorded."
        return "User not found."

    def log_diet(self, username, date, meal, calories):
        if username in self.users:
            diet_log = DietLog(date, meal, calories)
            self.users[username].diet.append(diet_log)
            return "Diet logged."
        return "User not found."

    def get_user_activities(self, username):
        if username in self.users:
            return [str(activity) for activity in self.users[username].activities]
        return "User not found."

    def get_user_diet(self, username):
        if username in self.users:
            return [str(diet) for diet in self.users[username].diet]
        return "User not found."

    def get_health_tips(self, username):
        if username not in self.users:
            return "User not found."
        user = self.users[username]
        bmi = user.bmi()
        if bmi < 18.5:
            return "Consider increasing your calorie intake to reach a healthy weight."
        elif bmi <= 24.9:
            return "Keep up the good work to maintain your healthy weight."
        elif bmi <= 29.9:
            return "Try to increase physical activity and adjust your diet to lose weight."
        else:
            return "Consider consulting a health professional to help manage your weight."

    def record_water_intake(self, username, date, amount):
        if username in self.users:
            self.users[username].record_water_intake(date, amount)
            return "Water intake recorded."
        return "User not found."

    def record_sleep_hours(self, username, date, hours):
        if username in self.users:
            self.users[username].record_sleep_hours(date, hours)
            return "Sleep hours recorded."
        return "User not found."

    def set_activity_goal(self, username, activity_type, goal):
        if username in self.users:
            self.users[username].set_activity_goal(activity_type, goal)
            return "Activity goal set."
        return "User not found."
