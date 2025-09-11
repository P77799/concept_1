movies=[]
s=int(input("How many movies do u wanna add?"))
for i in range(1,s+1):
    s2=input(f"enter the name of the movies-{i}:")
    movies.append(s2)
print(movies)
s3=input("do u wanna update? yes/no:")
if s3=="yes":
    up1=input("which movie do u wanna update?")
    if up1 in movies:
        up2=input("Enter the name of the movie :")
        ind=movies.index(up1)
        movies[ind]=up2
        print(movies)
