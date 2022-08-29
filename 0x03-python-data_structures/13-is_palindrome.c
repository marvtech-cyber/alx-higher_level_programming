#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singly list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reversed, *current;

	if (*head == NULL)
		return (1);

	reversed = reverse_listint(&reversed);
	current = *head;

	while (reversed && current)
	{
		if (current->n != reversed->n)
		{
			return (0);
		}
		reversed = reversed->next;
		current = current->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: singly list
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current, *next = NULL, *prev = NULL;

	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;

	return (*head);
}
