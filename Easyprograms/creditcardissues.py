credit_score = int(input('Enter the creditscore'))
if credit_score < 400 or credit_score > 850:
    print(f'Invalid credit score {credit_score}')
else:
    if credit_score >=400 and credit_score < 600:
        print(f'Sivler card {credit_score}')
    elif credit_score >=600 and credit_score < 800:
        print(f'Gold Card {credit_score}')
    else:
        print("Platinum Card")
