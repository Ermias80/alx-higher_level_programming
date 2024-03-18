#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Identifies if a singly linked list is palindrome
 * @head: Pointer to the head of listint_t
 * Return: 1 if it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;
	listint_t *mid = NULL;
	int is_pal = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	while (slow != NULL)
	{
		listint_t *temp = slow->next;
		slow->next = second_half;
		second_half = slow;
		slow = temp;
	}

	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_pal = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	slow = second_half;
	second_half = NULL;
	while (slow != NULL)
	{
		listint_t *temp = slow->next;
		slow->next = second_half;
		second_half = slow;
		slow = temp;
	}

	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (is_pal);
}
