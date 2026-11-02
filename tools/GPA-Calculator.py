import sys

# Toolkit Contract Metadata
AUTHOR = "Matthew Rakay"
APP_NAME = "GPA Calculator"

# Standard Letter Grade Scale
GRADE_SCALE = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0.0
}

def run():
    """Main execution function required by the toolkit contract."""
    print(f"--- {APP_NAME} by {AUTHOR} ---")
    print("Enter your courses. Type 'done' at the grade prompt when finished.\n")
    
    total_quality_points = 0.0
    total_credits = 0.0
    course_count = 1

    while True:
        grade_input = input(f"Enter Grade for Course #{course_count} (e.g., A, B+): ").strip().upper()
        if grade_input == 'DONE':
            break
            
        if grade_input not in GRADE_SCALE:
            print(f"❌ Invalid letter grade '{grade_input}'. Please choose a valid grade.")
            continue

        credit_input = input(f"Enter Credit Hours for Course #{course_count}: ").strip()

        # Acceptance Criteria: Reject non-numeric or negative credit values
        try:
            credits = float(credit_input)
            if credits < 0:
                print("❌ Invalid input: Credit hours cannot be negative.")
                continue
        except ValueError:
            print("❌ Invalid input: Credit hours must be a numeric value.")
            continue

        # Process valid inputs
        grade_value = GRADE_SCALE[grade_input]
        total_quality_points += (grade_value * credits)
        total_credits += credits
        course_count += 1
        print(f"Logged course with {credits} credits.\n")

    print("\n--- Evaluation Summary ---")
    if total_credits == 0:
        print("No valid courses were evaluated.")
    else:
        final_gpa = total_quality_points / total_credits
        print(f"Total Evaluated Credits: {total_credits}")
        print(f"Calculated Weighted GPA: {final_gpa:.2f}")

if __name__ == "__main__":
    run()
