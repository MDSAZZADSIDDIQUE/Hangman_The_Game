import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
random_word = random.choice(word_list)
output = []
for letter in random_word:
    output += "_"
display = f"{' '.join(output)}"
print(display)
end_of_game = False
lives = 6
while not end_of_game:
    guessed_letter = input("G U E S S   A   L E T T E R :   ").lower()
    for index in range(len(random_word)):
        if random_word[index] == guessed_letter:
            print("Y O U   H A V E   A L R E A D Y   G U E S S E D   T H E   W O R D . . .")
    for index in range(len(random_word)):
        if random_word[index] == guessed_letter:
            output[index] = guessed_letter
    if guessed_letter not in output:
        print("Y O U   H A V E   G U E S S E D   T H E   W R O N G   L E T T E R . . .")
        print("Y O U   H A V E   L O S T   A   L I F E . . .")
        lives -= 1
        if lives == 0:
            print("You Lose")
            end_of_game = True
    if "_" not in output:
        end_of_game = True
        print("You won")
    print(display)
    print(stages[lives])
