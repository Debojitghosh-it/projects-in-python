age = int(input("Enter your age here: "))
tck = True 

if age > 21:
    print("You can watch movie..")
elif age >= 15 and age <= 18:
    print("You can watch the movie with your parents..")
elif age < 15:
    print("You are not allowed to watch the movie")