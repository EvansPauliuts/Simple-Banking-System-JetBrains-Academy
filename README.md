# Simple-Banking-System-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/109

## Work on project. Stage 2/4: Luhn algorithm
### Objectives

You should allow customers to create a new account in our banking system.

Once the program starts, you should print the menu:

1. Create an account
2. Log into account
3. Exit
If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the conditions described above. 
Then you should generate a PIN code that belongs to the generated card number. The PIN code is a sequence of any 4 digits. 
PIN should be generated in a range from 0000 to 9999.

If the customer chooses ‘Log into account’, you should ask to enter the card information.

After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. 
It should also be possible to log out of the account and exit the program.

#### Examples
The greater-than symbol followed by a space (>) represents the user input.

```shell
1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000004938320896
Your card PIN:
6826

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000004938320896
Enter your PIN:
>4444

Wrong card number or PIN!

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000004938320896
Enter your PIN:
>6826

You have successfully logged in!

1. Balance
2. Log out
0. Exit
>1

Balance: 0

1. Balance
2. Log out
0. Exit
>2

You have successfully logged out!

1. Create an account
2. Log into account
0. Exit
>0

Bye!
```
