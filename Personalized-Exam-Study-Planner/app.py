import streamlit as st

from ocr import extract_text_from_pdf
from planner import create_study_plan


# --------------------------------------------------
# Page settings
# --------------------------------------------------

st.set_page_config(
    page_title="Personalized Exam Study Planner",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📚 Personalized Exam Study Planner")

st.write(
    "Upload your syllabus PDF and generate an "
    "exam-focused study plan with important questions."
)


# --------------------------------------------------
# Upload PDF
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your Syllabus PDF",
    type=["pdf"]
)


# --------------------------------------------------
# Number of preparation days
# --------------------------------------------------

days = st.number_input(
    "📅 How many days do you have for preparation?",
    min_value=1,
    max_value=100,
    value=7,
    step=1
)


# --------------------------------------------------
# Generate button
# --------------------------------------------------

if uploaded_file is not None:

    # Save uploaded PDF
    with open("uploaded.pdf", "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        "✅ PDF uploaded successfully!"
    )


    if st.button(
        "🚀 Generate Study Plan"
    ):

        # --------------------------------------------------
        # OCR
        # --------------------------------------------------

        with st.spinner(
            "📖 Reading your syllabus..."
        ):

            text = extract_text_from_pdf(
                "uploaded.pdf"
            )


        if not text.strip():

            st.error(
                "❌ Could not extract text from the PDF."
            )

        else:

            st.success(
                "✅ Syllabus processed successfully!"
            )


            # --------------------------------------------------
            # Create study plan
            # --------------------------------------------------

            plan = create_study_plan(
                text,
                days
            )


            # --------------------------------------------------
            # Display plan
            # --------------------------------------------------

            st.subheader(
                "📅 Your Personalized Study Plan"
            )


            if plan:

                for day in plan:

                    st.markdown(
                        "---"
                    )

                    st.markdown(
                        f"## 📅 Day {day['day']} — "
                        f"{day['date']}"
                    )


                    for topic_data in day["topics"]:

                        topic = topic_data["topic"]

                        questions = topic_data["questions"]


                        # ------------------------------------------
                        # Topic
                        # ------------------------------------------

                        st.markdown(
                            f"### 📖 {topic}"
                        )


                        st.markdown(
                            "#### 🔥 IMPORTANT QUESTIONS"
                        )


                        # ------------------------------------------
                        # Questions
                        # ------------------------------------------

                        high_questions = [
                            q for q in questions
                            if q["priority"] == "HIGH"
                        ]

                        medium_questions = [
                            q for q in questions
                            if q["priority"] == "MEDIUM"
                        ]


                        question_number = 1


                        # HIGH priority
                        for q in high_questions:

                            st.markdown(
                                f"**{question_number}. "
                                f"🔥 {q['question']}**"
                            )

                            question_number += 1


                        # MEDIUM priority
                        for q in medium_questions:

                            st.markdown(
                                f"{question_number}. "
                                f"⭐ {q['question']}"
                            )

                            question_number += 1


                        # ------------------------------------------
                        # Study priority
                        # ------------------------------------------

                        st.markdown(
                            "#### 📊 Study Priority"
                        )

                        st.write(
                            "🔥 HIGH — Study first"
                        )

                        st.write(
                            "⭐ MEDIUM — Study after HIGH priority questions"
                        )


                        # ------------------------------------------
                        # Study order
                        # ------------------------------------------

                        st.markdown(
                            "#### 📚 Study Order"
                        )

                        st.write(
                            "1️⃣ Learn the definition"
                        )

                        st.write(
                            "2️⃣ Learn the steps / method"
                        )

                        st.write(
                            "3️⃣ Study important concepts"
                        )

                        st.write(
                            "4️⃣ Practice the problems"
                        )

                        st.success(
                            f"✅ After completing {topic} "
                            f"questions → Move to the next topic."
                        )


            else:

                st.warning(
                    "⚠️ No topics were detected "
                    "from your syllabus."
                )


            # --------------------------------------------------
            # Optional OCR result
            # --------------------------------------------------

            with st.expander(
                "📄 View Extracted Syllabus Text"
            ):

                st.text_area(
                    "OCR Result",
                    text,
                    height=400
                )