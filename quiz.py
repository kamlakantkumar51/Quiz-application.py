class MahabharataQuiz:

    def _init_(self):
        self.questions = [
            {
                'question': 'Who was the eldest Pandava?',
                'options': ['Yudhishthira', 'Arjuna', 'Bhima', 'Nakula'],
                'answer': 'Yudhishthira'
            },
            {
                'question': 'Who was the guru of both the Pandavas and the Kauravas?',
                'options': ['Drona', 'Krishna', 'Vyasa', 'Bhishma'],
                'answer': 'Drona'
            },
            {
                'question': 'What was the name of the battle fought between the Pandavas and the Kauravas?',
                'options': ['Kurukshetra War', 'Mahabharata War', 'Dharma Yudhha', 'Brahma Yudhha'],
                'answer': 'Kurukshetra War'
            },
            {
                'question': 'Who was the charioteer of Arjuna during the Kurukshetra War?',
                'options': ['Bhishma', 'Krishna', 'Drona', 'Satyaki'],
                'answer': 'Krishna'
            },
            {
                'question': 'Who was the mother of the Kauravas?',
                'options': ['Kunti', 'Gandhari', 'Subhadra', 'Satyavati'],
                'answer': 'Gandhari'
            },
            {
                'question': 'What was the name of the weapon used by Arjuna to defeat Karna?',
                'options': ['Brahmastra', 'Vajra', 'Anjalika', 'Nagastra'],
                'answer': 'Anjalika'
            },
            {
                'question': 'Which of the following is NOT one of the Pandava brothers?',
                'options': ['Yudhishthira', 'Bhima', 'Duryodhana', 'Arjuna'],
                'answer': 'Duryodhana'
            },
            {
                'question': 'Who was the son of Karna?',
                'options': ['Abhimanyu', 'Vrishaketu', 'Ashwatthama', 'Ghatotkacha'],
                'answer': 'Vrishaketu'
            },
            {
                'question': 'Who was the first to fall in the battle of Kurukshetra?',
                'options': ['Bhishma', 'Duryodhana', 'Karna', 'Abhimanyu'],
                'answer': 'Bhishma'
            },
            {
                'question': 'What was the name of the eldest Kaurava?',
                'options': ['Duryodhana', 'Dushasana', 'Durmukha', 'Jaiadratha'],
                'answer': 'Duryodhana'
            }
        ]
        self.score = 0

    def display_question(self, q):
        print(f"\nQuestion: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")

    def get_answer(self, q):
        user_answer = input(f"Enter your answer (1-{len(q['options'])}): ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= len(q['options']):
                return q['options'][user_answer - 1]
            else:
                print("Invalid choice. Please try again.")
                return self.get_answer(q)
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your answer.")
            return self.get_answer(q)

    def run_quiz(self):
        print("Welcome to the Mahabharata Quiz!")
        for q in self.questions:
            self.display_question(q)
            user_answer = self.get_answer(q)
            if user_answer == q['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}")
        self.show_result()

    def show_result(self):
        print(f"\nYour final score is {self.score} out of {len(self.questions)}.")
        if self.score == len(self.questions):
            print("Excellent! You got all questions right.")
        elif self.score >= len(self.questions) // 2:
            print("Good job! You passed the quiz.")
        else:
            print("Better luck next time!")

if _name_ == "_main_":
    quiz = MahabharataQuiz()
    quiz.run_quiz()
