# Author: JD 09/28/2021

win_a = int(input("Please enter the number of wins for the first team: "))

tie_a = int(input("Please enter the number of ties for the first team: "))

win_b = int(input("Please enter the number of wins for the second team: "))

tie_b = int(input("Please enter the number of ties for the second team: "))

point_a = 3 * win_a + tie_a

point_b = 3 * win_b + tie_b

if point_a > point_b:
    print("The first team finished with more points")
else:
    print("The second team finished with more points")
