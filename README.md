### Personalized Exam Study Planner
Study Smart. Prioritize. Prepare.
Personalized Exam Study Planner is an educational application that uses PDF text extraction, OCR, and rule-based question analysis to convert a syllabus PDF into a structured, exam-focused study plan.
## Overview
The Personalized Exam Study Planner allows students to upload their syllabus PDF and enter the number of days available for preparation. The application extracts the syllabus content, identifies important topics and questions, assigns priorities, and creates a day-wise study plan.
Instead of simply displaying the syllabus, the application tells students what to study first, which questions are important, what problems to practice, and when to move to the next topic.
## Features
- Upload syllabus PDF
- Extract text from PDF
- Support scanned PDFs using Tesseract OCR
- Identify important syllabus topics
- Identify questions and problems from the syllabus
- Generate important exam questions
- Assign question priority
- ## HIGH priority questions for first preparation
-  ## MEDIUM priority questions for additional preparation
- Create day-wise study plans
- Automatically use the current date
- Provide a recommended study order
- Tell students when to move to the next topic
- Simple and user-friendly Streamlit interface
## How It Works
Syllabus PDF 

      |
      v
PDF Text Extraction

      |
      v
Tesseract OCR

      |
      v
Extracted Text

      |
      v
Topic Detection

      |
      v
Important Question Identification

      |
      v
Question Priority

      |
      v
Day-wise Study Plan

      |
      v
Student Preparation

## Example Output
 Day 1 — Simple Bar Diagram

 IMPORTANT QUESTIONS

1. Define Simple Bar Diagram.
2. Explain the steps to draw a Simple Bar Diagram.
3. Draw a Simple Bar Diagram for the given data.
4. Solve the problems based on Simple Bar Diagram.

## STUDY PRIORITY

## HIGH — Study first
## MEDIUM — Study after HIGH priority questions

## STUDY ORDER

1️ Learn the definition

2️ Learn the steps / method

3️ Study important concepts

4️ Practice the problems

## After completing Simple Bar Diagram
→ Move to the next topic.

## Technologies Used
Technology	Purpose

Python	Main programming language

Streamlit	Web application interface

PyMuPDF	PDF text extraction

Tesseract OCR	Scanned PDF text extraction

Pytesseract	Python OCR integration

Pillow	Image processing

Regular Expressions	Text cleaning and topic detection


## Project Structure
Personalized-Exam-Study-Planner/

|
├── app.py

├── ocr.py

├── planner.py

├── requirements.txt

├── README.md

└── uploaded.pdf

## Installation

Clone or download the repository and navigate to the project directory:

git clone <your-github-repository-url>

cd Personalized-Exam-Study-Planner

## Install the required packages:

pip install -r requirements.txt

Make sure Tesseract OCR is installed on your system.

For Windows, the default installation path is usually:

C:\Program Files\Tesseract-OCR

## Check the installation:

tesseract --version

## Run the Application

Run the Streamlit application using:

python -m streamlit run app.py

The application will open in your browser.

## Usage
1. Upload your syllabus PDF.
2. Enter the number of preparation days.
3. Click Generate Study Plan.
4. The system extracts the syllabus content.
5. Topics and important questions are identified.
6. Questions are assigned priorities.
7. A personalized day-wise study plan is displayed.
8. Complete the important questions before moving to the next topic.
   
## Current Topics

The planner currently supports topics such as:
1. Simple Bar Diagram
2. Multiple Bar Diagram
3. Pie Diagram
4. Histogram
5. Frequency Polygon
6. Frequency Curve
7. Ogive Curve

## Question Priority
## HIGH Priority
Questions that should be studied first:
- Definitions
- Important steps
- Formulas and calculations
- Diagram-based questions
- Numerical problems
- Problems provided in the syllabus
## MEDIUM Priority
Questions to study after HIGH priority questions:
- Uses
- Additional concepts
- Supporting theory
Safety / Educational Notice
This application is designed for educational purposes. The generated study plan is intended to help students organize their exam preparation and should be used along with their official syllabus, class notes, textbooks, and guidance from their faculty.
## Future Enhancements
-  AI-based question generation
-  Previous-year question analysis
-  Automatic important-question ranking
-  Study-time estimation
-  Student progress tracking
-  Question completion tracking
-  Automatic revision schedule
-  Previous-year question paper integration
-  Mobile-friendly interface
-  LLM-based personalized study recommendations
## Author
## LATTIKHASHRI.N

## B.Sc. Computer Science with Artificial Intelligence
## Project : Personalized Exam Study Planner
## Project Type: Academic / College Project
## Domain: Artificial Intelligence / Natural Language Processing / Education Technology
## app link:http://localhost:8501/
