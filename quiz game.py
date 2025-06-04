import time
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
                "answer": "B"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "B"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
                "answer": "B"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
                "answer": "C"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["A. Go", "B. Au", "C. Ag", "D. Gd"],
                "answer": "B"
            }
        ]
        self.score = 0
        self.total_questions = len(self.questions)
    
    def display_welcome(self):
        print(Fore.CYAN + "\n" + "="*50)
        print(Fore.YELLOW + "Welcome to the Python Quiz Game!")
        print(Fore.CYAN + "="*50)
        print(Fore.GREEN + f"\nYou will be presented with {self.total_questions} multiple-choice questions.")
        print("Try to answer as many as you can correctly!\n")
        input("Press Enter to start the quiz...")
        print("\n")
    
    def ask_question(self, question_data):
        print(Fore.BLUE + question_data["question"])
        for option in question_data["options"]:
            print(Fore.WHITE + option)
        
        while True:
            user_answer = input(Fore.YELLOW + "\nYour answer (A/B/C/D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print(Fore.RED + "Invalid input! Please enter A, B, C, or D.")
        
        correct_answer = question_data["answer"]
        
        if user_answer == correct_answer:
            print(Fore.GREEN + "\nCorrect!" + Style.RESET_ALL)
            self.score += 1
        else:
            print(Fore.RED + f"\nIncorrect! The correct answer is {correct_answer}." + Style.RESET_ALL)
        
        time.sleep(1.5)
        print("\n" + "-"*50 + "\n")
    
    def show_results(self):
        print(Fore.CYAN + "\n" + "="*50)
        print(Fore.YELLOW + "Quiz Results:")
        print(Fore.CYAN + "="*50)
        
        percentage = (self.score / self.total_questions) * 100
        
        print(Fore.WHITE + f"\nYour final score: {self.score}/{self.total_questions}")
        print(Fore.WHITE + f"Percentage: {percentage:.1f}%")
        
        if percentage >= 80:
            print(Fore.GREEN + "\nExcellent! You're a quiz master!")
        elif percentage >= 60:
            print(Fore.YELLOW + "\nGood job! You know quite a lot.")
        elif percentage >= 40:
            print(Fore.MAGENTA + "\nNot bad! Keep learning.")
        else:
            print(Fore.RED + "\nKeep practicing! You'll do better next time.")
        
        print("\nThanks for playing!\n")
    
    def run_quiz(self):
        self.display_welcome()
        
        for i, question in enumerate(self.questions, 1):
            print(Fore.MAGENTA + f"Question {i}/{self.total_questions}")
            self.ask_question(question)
        
        self.show_results()

if __name__ == "__main__":
    # Install colorama if not already installed
    try:
        from colorama import Fore
    except ImportError:
        import subprocess
        subprocess.check_call(["pip", "install", "colorama"])
        from colorama import Fore, Style, init
        init(autoreset=True)
    
    quiz = QuizGame()
    quiz.run_quiz()