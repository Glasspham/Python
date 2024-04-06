# Bài 1
i = 1
while i <= 50:
    print(i)
    i += 1

# Bài 2
s = input().split()
i = 0
while i < len(s):
    print(s[i], end=' ') 
    i += 1

# Bài 3
s = input().split()
i = 1
while i < len(s):
    print(s[i], end=" ")
    i += 2

# Bài 4
kg = float(input())
while kg < 0:
    print("Không hợp lệ")
    kg = float(input())
pound = kg * 2.20462
print(pound)

# Bài 5
n = 5
while n:
    password = input()
    if password == "123":
        print("Welcome")
        break
    else:
        print("Try again")
    if n == 1:
        print("You have no more chance")
    n -= 1

# Bài 6
A = []
cnt = 0
input_str = input("Nhập điểm, cách nhau bởi dấu cách (dừng khi gặp giá trị âm): ")
input_list = input_str.split()  
i = 0
while i < len(input_list):
    n = int(input_list[i])
    if n < 0:
        break
    A.append(n)
    if n >= 9:
        cnt += 1
    i += 1

if len(A) > 0:
    print("Số điểm A là:", cnt)
    print("Điểm trung bình là:", sum(A) / len(A))
else:
    print("Không có điểm nào được nhập.")



# Bài 7
import random
words = ["hello", "world", "apple", "banana", "python", "programming", "elephant", "giraffe", "computer", "keyboard"]
selected_word = None
while selected_word is None:
    word = random.choice(words)
    unique_chars = set(word)
    if len(word) == len(unique_chars):
        selected_word = word
print("Từ được chọn ngẫu nhiên không có chữ cái lặp lại là:", selected_word)

# Bài 8
import random
money = 100
while money > 0 and money < 200:
    guess = input("Ngửa (N) hay Sấp (S)? ").upper()
    coin = random.choice(["N", "S"])
    if guess == coin:
        money += 9
        print(f"Bạn đoán đúng! Tiền của bạn hiện tại là ${money}.")
    else:
        money -= 10
        print(f"Bạn đoán sai! Tiền của bạn hiện tại là ${money}.")

if money <= 0:
    print("Bạn đã hết tiền. Game over!")
else:
    print("Chúc mừng! Bạn đã chiến thắng và kiếm được $200.")



# Bài 9
import random

countries = ["CANADA", "UNITED STATES", "UNITED KINGDOM", "FRANCE", "GERMANY", "ITALY"]
country = random.choice(countries).upper()
guessed_letters = []
wrong_guesses = 0

while wrong_guesses < 5 and "-" in ''.join(letter if letter in guessed_letters else '- ' for letter in country):
    display = ''.join(letter if letter in guessed_letters else '- ' for letter in country)
    print(display.strip())
    guess = input("Đoán một chữ cái: ").upper()

    if guess in guessed_letters:
        print("Bạn đã đoán chữ cái này rồi.")
    elif guess in country:
        guessed_letters.append(guess)
        print("Chính xác!")
    else:
        wrong_guesses += 1
        print("Sai chữ cái. Số lần đoán sai: ", wrong_guesses)

if "-" not in ''.join(letter if letter in guessed_letters else '- ' for letter in country):
    print("Chúc mừng! Bạn đã đoán đúng từ", country)
else:
    print("Bạn đã thua. Từ cần đoán là", country)

