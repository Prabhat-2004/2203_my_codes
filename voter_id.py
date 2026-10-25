age = int(input("Enter your age: "))
if age >= 18:
    having_voter_id = input("Have you a voter id: (Yes or No): ").lower()
    if having_voter_id == "yes":
        print("Eligible for vote")
    else:
        print("Voter id required")
else:
    print("Not eligible for vote")