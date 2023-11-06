#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Pointer to pointer to head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i = 0;
	int count = 0;
	int *values;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);

	while (current)
	{
		count++;
		current = current->next;
	}

	values = malloc(sizeof(int) * count);
	if (values == NULL)
		return (NULL);

	current = *head;
	while (current)
	{
		values[i++] = current->n;
		current = current->next;
	}

	for (i = 0; i < count / 2; i++)
	{
		if (values[i] != values[count - 1 - i])
		{
			free(values);
			return (0);
		}
	}

	free(values);
	return (1);

}
