#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - the function that does the insterting of the node
 * @head: the pointer to the pointer of the head
 * @number: the number to be insterted
 * Return: the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *previous = NULL;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (current == NULL)
	{
		*head = new;
	}
	else
	{
		while (current != NULL)
		{
			if (number < current->n)
			{
				if (previous == NULL)
				{
					new->next = current;
					*head = new;
				}
				else
				{
					previous->next = new;
					new->next = current;
				}
				break;
			}
			previous = current;
			current = current->next;
		}
		if (current == NULL)
		{
			previous->next = new;
		}
	}
	return (new);
}
