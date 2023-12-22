#include "sort.h"

/**
 * swap - Function that swap the position of two element
 * @a: first element
 * @b: second element
 * Return: Nothing
 */
void swap(int *a, int *b)
{
	int tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

/**
 * heapify - FUnction that create a max heap
 * @array: the array
 * @n: the size of the array
 * @i: the index of non-leaf node
 * @size: the size of the array for print function
 * Return: Nothing
 */
void heapify(int *array, int n, int i, size_t size)
{
	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < n && array[left] > array[largest])
		largest = left;
	if (right < n && array[right] > array[largest])
		largest = right;

	if (largest != i)
	{
		swap(&array[i], &array[largest]);
		print_array(array, size);
		heapify(array, n, largest, size);
	}
}

/**
 * heap_sort - Function that sorts an array of integers in ascending
 * order using the Heap sort method
 * @array: the array
 * @size: the size of the array
 * Return: Nothing
 */
void heap_sort(int *array, size_t size)
{
	int i;
	/* Build max heap */
	for (i = size / 2 - 1; i >= 0; i--)
		heapify(array, size, i, size);

	for (i = size - 1; i > 0; i--)
	{
		swap(&array[0], &array[i]);
		print_array(array, size);
		heapify(array, i, 0, size);
	}
}
