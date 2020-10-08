from mongodb import collection

def subjects(results):
    for result in results:
        subject1 = result["subject1"]
        subject2 = result["subject2"]
        subject3 = result["subject3"]
        subject4 = result["subject4"]
        subject5 = result["subject5"]

        subjects1 = subject1 + "\n" + subject2 + "\n" + subject3 + "\n" + subject4 + "\n" + subject5 + "\n"
        print(subjects1)
results = collection.find({"day": "monday"})
subjects(results)
