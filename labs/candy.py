coupons = int(input("Enter amount of coupons: "));
couponsCandybar = 10;
couponsGumball = 3;

candybars = coupons // couponsCandybar;
gumballs = (coupons % couponsCandybar) // couponsGumball;

if coupons < 0:
	candybars = 0;
	gumballs = 0;

print("You can buy " + str(candybars) + " candy bar(s)!");
print("You can also buy " + str(gumballs) + " gumball(s)!");
