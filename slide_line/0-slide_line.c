#include "slide_line.h"

/**
 * merge_left - Merge same values on the left
 */
void merge_left(int *line, int size)
{
	int i, j, tmp = 0;

	for (i = 0; i < size; i++)
	{
		if (line[i] != 0)
		{
			if (line[i] == tmp)
			{
				line[i] = 2 * line[i];
				line[j] = 0;
				tmp = 0;
			}
			else if (line[i] != tmp && i <= size - 1)
			{
				j = i;
				tmp = line[i];
			}
		}
	}
}

/**
 * merge_right - Merge same values on the right
 */
void merge_right(int *line, int size)
{
	int i, j, tmp = 0;

	for (i = size - 1; i > -1; i--)
	{
		if (line[i] != 0)
		{
			if (line[i] == tmp)
			{
				line[i] = 2 * line[i];
				line[j] = 0;
				tmp = 0;
			}
			else if (line[i] != tmp && i > 0)
			{
				j = i;
				tmp = line[i];
			}
		}
	}
}

/**
 * slide_left - Slide numbers on the left
 */
void slide_left(int *line, size_t size)
{
	size_t i, j;

	for (i = 0; i < size - 1; i++)
	{
		if (line[i] == 0)
		{
			j = i;
			while (line[i] == 0 && j < size)
			{
				if (line[j] != 0)
				{
					line[i] = line[j];
					line[j] = 0;
				}
				j++;
			}
		}
	}
}

/**
 * slide_right - Slide numbers on the right
 */
void slide_right(int *line, int size)
{
	int i, j;

	for (i = size - 1; i > -1; i--)
	{
		if (line[i] == 0)
		{
			j = i;
			while (line[i] == 0 && j > -1)
			{
				if (line[j] != 0)
				{
					line[i] = line[j];
					line[j] = 0;
				}
				j--;
			}
		}
	}
}

/**
 * slide_line - Reproduce the 2048 game mechanics on a single horizontal line
 */
int slide_line(int *line, size_t size, int direction)
{
	if (direction == SLIDE_LEFT)
	{
		merge_left(line, size);
		slide_left(line, size);
	}
	else if (direction == SLIDE_RIGHT)
	{
		merge_right(line, size);
		slide_right(line, size);
	}
	else
		return (0);
	return (1);
}
