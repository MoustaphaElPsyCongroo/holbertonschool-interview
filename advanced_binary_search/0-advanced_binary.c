#include "search_algos.h"

/**
 * print_array - function that print an array
 * @array: an array
 * @left: the beginning of the array
 * @right: the end of the array
 * Return: Nothing
 */
void print_array(int *array, size_t left, size_t right)
{
	size_t i;

	printf("Searching in array: ");
	for (i = left; i <= right; i++)
	{
		printf("%d", array[i]);
		if (i != right)
			printf(", ");
	}
	printf("\n");
}

/**
 * binary_search_left - Function that searches the first occurrence of a value
 * @array: Pointer to the first element of the array
 * @left: The left index of the search range
 * @right: The right index of the search range
 * @value: The value to search for
 * Return: The index of the first occurrence of the value
 *         or -1 if value not found
 */
int binary_search_left(int *array, size_t left, size_t right, int value)
{
	size_t mid;

	print_array(array, left, right);

	if (left > right || left == right)
		return (-1);

	if (value == array[left])
		return (left);

	mid = left + (right - left) / 2;

	if (value > array[mid])
		return (binary_search_left(array, mid + 1, right, value));
	else
		return (binary_search_left(array, left, mid, value));
}

/**
 * advanced_binary - Function that searches for a value in an sorted of
 * integers using Advanced Binary Search Algorithm
 * @array: Pointer to the first element of the array
 * @size: The number of elements in array
 * @value: The value to search for
 * Return: The first index where value is located
 *         -1 if value is not present in array
 *         -1 if array is NULL
 */
int advanced_binary(int *array, size_t size, int value)
{
	if (array == NULL || size == 0)
		return (-1);

	return (binary_search_left(array, 0, size - 1, value));
}
