# MCQ_generator
Python
License
Contributions Welcome
The MCQ Generator is a Python-based tool designed to automatically generate Multiple Choice Questions (MCQs) from a given text or document. It uses Natural Language Processing (NLP) techniques to extract key information and create questions, making it a valuable tool for educators, content creators, and learners.

Features
Text-to-MCQ Conversion: Automatically generates MCQs from input text.

Customizable Question Types: Supports different types of questions (e.g., fill-in-the-blank, true/false, multiple-choice).

Easy-to-Use Interface: Simple command-line interface for quick usage.

Export Options: Save generated questions in various formats (e.g., JSON, CSV, or plain text).

NLP-Powered: Utilizes advanced NLP libraries for accurate question generation.

Installation
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Steps
Clone the repository:

bash
Copy
git clone https://github.com/nikhilbudhathoki/MCQ_generator.git
cd MCQ_generator
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Usage
Command-Line Interface
Run the MCQ generator from the command line:

bash
Copy
python mcq_generator.py --input "path/to/input.txt" --output "path/to/output.json"
Arguments:
--input: Path to the input text file or directory.

--output: Path to save the generated MCQs (default: output.json).

--num_questions: Number of questions to generate (default: 10).

Example
bash
Copy
python mcq_generator.py --input sample_text.txt --output questions.json --num_questions 5
How It Works
Text Preprocessing: The input text is cleaned and tokenized.

Keyphrase Extraction: Important phrases and concepts are identified using NLP techniques.

Question Generation: Questions are formed based on the extracted keyphrases.

Answer Generation: Distractors (incorrect answers) are generated, and the correct answer is identified.

Output: The generated MCQs are saved in the specified format.

File Structure
Copy
MCQ_generator/
├── mcq_generator.py       # Main script for generating MCQs
├── requirements.txt       # List of dependencies
├── sample_text.txt        # Example input text
├── questions.json         # Example output file
├── README.md              # This file
└── LICENSE                # License information
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Built using Python and NLP libraries like spaCy, nltk, and transformers.

Inspired by the need for automated question generation in education.

Contact
For questions or feedback, feel free to reach out:

Nikhil Budhathoki

Email: your.email@example.com

GitHub: nikhilbudhathoki

