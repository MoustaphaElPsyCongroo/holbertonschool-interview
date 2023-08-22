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
	listint_t *current = *head;
	listint_t *new_node;

	if (head == NULL)
		return (NULL);

	if (*head == NULL || number < (*head)->n)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);

		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current != NULL)
	{
		if (current->next != NULL && number <= current->next->n)
		{
			listint_t *next = current->next;

			new_node = malloc(sizeof(listint_t));

			if (new_node == NULL)
				return (NULL);

			new_node->n = number;
			new_node->next = next;
			current->next = new_node;
			return (new_node);
		}

		current = current->next;
	}

	return (NULL);
}
