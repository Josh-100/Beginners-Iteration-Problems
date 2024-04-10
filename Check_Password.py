correct_password = "Pineapple"
for num in range(3):
    guess = input("Guess the password!: ")
    if guess == correct_password:
        print("Yay you got it right! The correct password was indeed 'Pineapple'.")
        break
    else:
        if num!= 2:
            print(f"Nope! Try again! Guess number {num+2}: ")
        else:
            print("All three tries failed. LOCKED OUT")