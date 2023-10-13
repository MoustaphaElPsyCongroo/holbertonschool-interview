#include "palindrome.h"

/**
 * is_palindrome - main function
 * @n: the number to check
 * Return: 1 if n is palindrome else 0
 */

int is_palindrome(unsigned long n)
{
	unsigned long reminder, reversed = 0, num = n;

	while (num != 0)
	{
		reminder = num % 10;
		reversed = reversed * 10 + reminder;
		num = num / 10;
	}

	return reversed == n;
}
