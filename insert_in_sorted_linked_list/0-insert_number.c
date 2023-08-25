#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Head of the list
 * @number: Number to insert
 *
 * Return: The address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current;

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}

	current = *head;

	if (number < (*head)->n)
	{
		*head = new_node;
		new_node->next = current;
		return (new_node);
	}

	while (current->next != NULL)
	{
		/* code */
		if (number < current->next->n)
		{
			listint_t *next = current->next;
			current->next = new_node;
			new_node->next = next;
			return (new_node);
		}

		current = current->next;
	}

	current->next = new_node;
	return (NULL);
}
