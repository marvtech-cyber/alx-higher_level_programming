#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: singly list
 * @number: int to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *current = *head;

/* allocate memory */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

/* find the place to insert, number must be in croissant order */
	while (current && number > current->n)
	{
		tmp = current;
		current = current->next;
	}

	new->n = number;

/* empty list */
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = current;
		if (current == *head) /* first node */
			*head = new;
		else
			tmp->next = new;
	}

	return (new);
}
