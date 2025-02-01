class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        total = 0
        count = 0
        for score in self.scores:
            total += score
            count += 1
        average = total / count
        return average

    def is_passing(self):
        for score in self.scores:
            if score < 40:
                return False
        return True


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students[name] = student

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = 0
        student_count = 0
        for student in self.students.values():
            total_average += student.calculate_average()
            student_count += 1
        class_average = total_average / student_count
        return class_average

    def display_student_performance(self):
        print("\n--- Student Performance ---")
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{student.name}: Average Score = {average:.2f}, Status = {status}")
        class_average = self.calculate_class_average()
        print(f"\nClass Average Score: {class_average:.2f}")


def get_student_input(tracker):
    while True:
        name = input("\nEnter the student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        scores = []
        for subject in ["Math", "Science", "English"]:
            while True:
                try:
                    score = int(input(f"Enter {name}'s score in {subject}: "))
                    scores.append(score)
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")
        tracker.add_student(name, scores)


def main():
    print("Welcome to the Student Performance Tracker!")
    tracker = PerformanceTracker()
    get_student_input(tracker)
    tracker.display_student_performance()


main()
