DISEASE_NAME = ["Common Cold", "Diabetes", "Bronchitis", "Influenza", "Kidney Stones"]
DIAGNOSED_PATIENTS = [320, 120, 100, 150, 60]

disease_counts = dict(zip(DISEASE_NAME, DIAGNOSED_PATIENTS))

max_disease = max(disease_counts, key=disease_counts.get)

print(f"The most common disease is: {max_disease} with {disease_counts[max_disease]} diagnosed patients.")
