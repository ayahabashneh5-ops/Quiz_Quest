import random

questions = [
    {
        "question": "ما عاصمة الأردن؟",
        "options": ["أ- عمان", "ب- إربد", "ج- الكرك"],
        "answer": "أ"
    },
    {
        "question": "كم عدد أيام السنة العادية؟",
        "options": ["أ- 300", "ب- 365", "ج- 400"],
        "answer": "ب"
    },
    {
        "question": "ما الكوكب المعروف بالكوكب الأحمر؟",
        "options": ["أ- الأرض", "ب- الزهرة", "ج- المريخ"],
        "answer": "ج"
    },
    {
        "question": "ما أكبر محيط في العالم؟",
        "options": ["أ- الهادئ", "ب- الأطلسي", "ج- الهندي"],
        "answer": "أ"
    },
    {
        "question": "كم عدد ألوان قوس قزح؟",
        "options": ["أ- خمسة", "ب- سبعة", "ج- تسعة"],
        "answer": "ب"
    }
]

random.shuffle(questions)

score = 0

print("================================")
print("   مرحباً بك في لعبة تحدي المعلومات")
print("================================")

for i, question in enumerate(questions, 1):
    print("\nالسؤال رقم:", i)
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("اختر الإجابة: ").strip().upper()

    if answer == question["answer"]:
        print("إجابة صحيحة! أحسنت.")
        score += 1
    else:
        print("إجابة خاطئة!")

print("\n================================")
print("انتهت اللعبة!")
print("نتيجتك:", score, "من", len(questions))

if score == 5:
    print("ممتاز! أنت بطل المعلومات!")
elif score >= 3:
    print("أحسنت! نتيجة جيدة.")
else:
    print("حاول مرة أخرى!")

print("شكراً لمشاركتك في اللعبة!")
print("================================")
