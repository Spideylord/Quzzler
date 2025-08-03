# Quizzler - Trivia Quiz App

A interactive trivia quiz application built with Python using the `tkinter` library. Quizzler fetches true/false questions from the Open Trivia Database API and allows users to answer them through a graphical interface, tracking their score as they go.

## Project Structure

- **main.py**: Entry point of the application, initializing the question bank, quiz logic, and UI.
- **data.py**: Fetches quiz questions from the Open Trivia Database API and stores them in `question_data`.
- **ui.py**: Implements the graphical user interface using `tkinter`, including the question display, buttons, and score tracking.
- **quiz_brain.py**: Manages the quiz logic, including question progression and score calculation.
- **question_model.py**: Defines the `Question` class to structure question data.
- **images/true.png**: Image for the "True" button.
- **images/false.png**: Image for the "False" button.

## Prerequisites

To run the application, you need Python installed along with the following libraries:

- `tkinter` (standard library, included with Python)
- `requests` (for API calls)

Install the required library using pip:

```bash
pip install requests
```

Ensure the `images/true.png` and `images/false.png` files are present in the `images` directory (or adjust the file paths in `ui.py` if using different images).

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd quizzler
   ```

3. Install the required library:

   ```bash
   pip install requests
   ```

4. Ensure the `images` directory contains `true.png` and `false.png` files (you can replace them with your own images if needed).

5. Run the application:

   ```bash
   python main.py
   ```

## Features

- **Dynamic Questions**: Fetches 10 true/false questions from the Open Trivia Database API.
- **Interactive UI**: Displays questions on a canvas with "True" and "False" buttons for answers.
- **Score Tracking**: Updates and displays the score in real-time.
- **Feedback**: Highlights correct (green) or incorrect (red) answers for 1 second before moving to the next question.
- **Completion**: Ends the quiz when all questions are answered, showing the final score.

## Usage

- Click "True" or "False" to answer each question.
- The canvas background turns green for correct answers or red for incorrect ones, then automatically proceeds to the next question after 1 second.
- The score is updated and displayed at the top right.
- Once all questions are answered, the interface shows a completion message, and the buttons are disabled.

## File Descriptions

- **main.py**: Initializes the question bank from `data.py`, creates a `QuizBrain` instance, and launches the `QuizUi`.
- **data.py**: Uses the `requests` library to fetch 10 boolean-type questions from the Open Trivia Database API, storing them in `question_data`.
- **ui.py**: Sets up the `tkinter` window with a canvas for questions, buttons for answers, and a score label, handling user input and feedback.
- **quiz_brain.py**: Manages the quiz flow, tracking the question number, score, and checking user answers.
- **question_model.py**: Defines the `Question` class with `text` and `answer` attributes.

## Notes

- The app fetches questions dynamically from the Open Trivia Database (https://opentdb.com/api.php), requiring an internet connection.
- The default question set is limited to 10 boolean questions; modify the `params` in `data.py` to adjust the amount or type.
- Ensure the `images` directory and its contents are correctly placed relative to `main.py`.
- The quiz ends automatically when all questions are answered, displaying the final score in the console.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.