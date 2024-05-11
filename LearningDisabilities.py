knowledge_base = {
    'reading difficulties': 'dyslexia',
    'difficulty with phonological awareness': 'dyslexia',
     'difficulty with phonological awareness': 'dyslexia',
    'difficulty with letter recognition': 'dyslexia',
    'poor spelling skills': 'dyslexia',
    'difficulty with decoding words': 'dyslexia',
    'slow reading rate': 'dyslexia',
    'difficulty with reading comprehension': 'dyslexia',
    'reversing letters or numbers': 'dyslexia',
    'difficulty with sequencing': 'dyslexia',
    'avoiding reading or writing tasks': 'dyslexia',
    # Add more symptom-condition mappings as needed
}

def diagnose(symptoms):
    for symptom in symptoms:
        if symptom in knowledge_base:
            return knowledge_base[symptom]
    return "No specific learning disability identified."

def main():
    print("Welcome to the Learning Disability Expert System")
    print("Please describe the child's symptoms (comma-separated):")
    symptoms = input().split(',')
    diagnosis = diagnose(symptoms)
    print("Diagnosis:", diagnosis)

if __name__ == "__main__":
    main()
