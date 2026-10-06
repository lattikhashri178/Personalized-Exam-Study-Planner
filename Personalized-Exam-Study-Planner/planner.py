from datetime import date, timedelta
import re


# --------------------------------------------------
# Clean OCR text
# --------------------------------------------------

def clean_text(text):
    # Remove dates such as June 22, 2026
    text = re.sub(
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)'
        r'\s+\d{1,2},\s+\d{4}\b',
        '',
        text,
        flags=re.IGNORECASE
    )

    # Remove UNIT headings
    text = re.sub(
        r'\bUNIT\s+[IVX]+\b',
        '',
        text,
        flags=re.IGNORECASE
    )

    # Remove page numbers such as 1/30
    text = re.sub(r'\b\d+\s*/\s*\d+\b', '', text)

    return text


# --------------------------------------------------
# Topics we expect in the syllabus
# --------------------------------------------------

TOPICS = [
    "Simple Bar Diagram",
    "Multiple Bar Diagram",
    "Pie Diagram",
    "Histogram",
    "Frequency Polygon",
    "Frequency Curve",
    "Ogive Curve"
]


# --------------------------------------------------
# Questions for each topic
# --------------------------------------------------

QUESTION_BANK = {

    "Simple Bar Diagram": [
        ("Define Simple Bar Diagram.", "HIGH"),
        ("Explain the steps to draw a Simple Bar Diagram.", "HIGH"),
        ("What are the uses of a Simple Bar Diagram?", "MEDIUM"),
        ("Draw a Simple Bar Diagram for the given data.", "HIGH"),
        ("Solve the problems based on Simple Bar Diagram given in the syllabus.", "HIGH")
    ],

    "Multiple Bar Diagram": [
        ("Define Multiple Bar Diagram.", "HIGH"),
        ("Explain the steps to draw a Multiple Bar Diagram.", "HIGH"),
        ("What are the uses of a Multiple Bar Diagram?", "MEDIUM"),
        ("Draw a Multiple Bar Diagram for the given data.", "HIGH"),
        ("Solve the problems based on Multiple Bar Diagram given in the syllabus.", "HIGH")
    ],

    "Pie Diagram": [
        ("Define Pie Diagram.", "HIGH"),
        ("Explain the steps to construct a Pie Diagram.", "HIGH"),
        ("Explain how to calculate the angle for each sector.", "HIGH"),
        ("What are the uses of a Pie Diagram?", "MEDIUM"),
        ("Draw a Pie Diagram for the given data.", "HIGH"),
        ("Solve the problems based on Pie Diagram given in the syllabus.", "HIGH")
    ],

    "Histogram": [
        ("Define Histogram.", "HIGH"),
        ("Explain the steps to construct a Histogram.", "HIGH"),
        ("Explain the difference between Histogram and Bar Diagram.", "HIGH"),
        ("Explain class intervals and class boundaries used in a Histogram.", "HIGH"),
        ("Draw a Histogram for the given data.", "HIGH"),
        ("Solve the problems based on Histogram given in the syllabus.", "HIGH")
    ],

    "Frequency Polygon": [
        ("Define Frequency Polygon.", "HIGH"),
        ("Explain the steps to construct a Frequency Polygon.", "HIGH"),
        ("What is a class mark? Explain with an example.", "HIGH"),
        ("Explain how class marks are calculated.", "HIGH"),
        ("Draw a Frequency Polygon for the given data.", "HIGH"),
        ("Solve the problems based on Frequency Polygon given in the syllabus.", "HIGH")
    ],

    "Frequency Curve": [
        ("Define Frequency Curve.", "HIGH"),
        ("Explain the steps to construct a Frequency Curve.", "HIGH"),
        ("Explain the difference between Frequency Polygon and Frequency Curve.", "MEDIUM"),
        ("Draw a Frequency Curve for the given data.", "HIGH"),
        ("Solve the problems based on Frequency Curve given in the syllabus.", "HIGH")
    ],

    "Ogive Curve": [
        ("Define Ogive Curve.", "HIGH"),
        ("Explain the steps to construct an Ogive Curve.", "HIGH"),
        ("What are the types of Ogive Curves?", "HIGH"),
        ("Explain Less Than Ogive.", "HIGH"),
        ("Explain More Than Ogive.", "HIGH"),
        ("What are the uses of Ogive Curve?", "HIGH"),
        ("Draw an Ogive Curve for the given data.", "HIGH"),
        ("Solve the problems based on Ogive Curve given in the syllabus.", "HIGH")
    ]
}


# --------------------------------------------------
# Find topics in the PDF
# --------------------------------------------------

def find_topics(text):

    text_lower = text.lower()

    found_topics = []

    for topic in TOPICS:

        if topic.lower() in text_lower:
            found_topics.append(topic)

    return found_topics


# --------------------------------------------------
# Find actual problem/question text from PDF
# --------------------------------------------------

def find_pdf_questions(text, topic):

    questions = []

    lines = text.splitlines()

    topic_found = False

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Start when topic is found
        if topic.lower() in line.lower():
            topic_found = True
            continue

        # Stop when another major topic begins
        for other_topic in TOPICS:

            if (
                other_topic != topic
                and other_topic.lower() in line.lower()
            ):
                topic_found = False

        if not topic_found:
            continue

        # Detect common question/problem lines
        if re.search(
            r'^(problem|question|example|\d+[\.\)])',
            line,
            re.IGNORECASE
        ):

            if len(line) > 15 and len(line) < 500:

                questions.append(line)

    return questions


# --------------------------------------------------
# Remove duplicate questions
# --------------------------------------------------

def remove_duplicates(questions):

    result = []
    seen = set()

    for question in questions:

        key = question.lower().strip()

        if key not in seen:

            seen.add(key)
            result.append(question)

    return result


# --------------------------------------------------
# Create questions for a topic
# --------------------------------------------------

def create_topic_questions(text, topic):

    questions = []

    # Add standard important questions
    for question, priority in QUESTION_BANK.get(topic, []):

        questions.append({
            "question": question,
            "priority": priority
        })

    # Find questions/problems from PDF
    pdf_questions = find_pdf_questions(text, topic)

    for question in pdf_questions:

        questions.append({
            "question": question,
            "priority": "HIGH"
        })

    # Remove duplicate questions
    final_questions = []

    seen = set()

    for item in questions:

        key = item["question"].lower().strip()

        if key not in seen:

            seen.add(key)
            final_questions.append(item)

    return final_questions


# --------------------------------------------------
# Create complete study plan
# --------------------------------------------------

def create_study_plan(text, days):

    text = clean_text(text)

    topics = find_topics(text)

    if not topics:
        return []

    today = date.today()

    plan = []

    total_topics = len(topics)

    # If fewer days than topics,
    # put multiple topics into some days.
    topics_per_day = max(1, total_topics // days)

    topic_index = 0

    for day_number in range(1, days + 1):

        if topic_index >= total_topics:
            break

        current_topics = []

        # Calculate how many topics should be on this day
        remaining_topics = total_topics - topic_index
        remaining_days = days - day_number + 1

        number_for_today = max(
            1,
            (remaining_topics + remaining_days - 1)
            // remaining_days
        )

        for _ in range(number_for_today):

            if topic_index >= total_topics:
                break

            topic = topics[topic_index]

            questions = create_topic_questions(
                text,
                topic
            )

            current_topics.append({
                "topic": topic,
                "questions": questions
            })

            topic_index += 1

        plan.append({
            "day": day_number,
            "date": (
                today + timedelta(days=day_number - 1)
            ).strftime("%d %B %Y"),

            "topics": current_topics
        })

    return plan