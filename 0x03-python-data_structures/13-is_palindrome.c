#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid = NULL;
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

    listint_t *second_half = slow;
    prev_slow->next = NULL;
    reverse_list(&second_half);
    is_pal = compare_lists(*head, second_half);
    reverse_list(&second_half);

    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = second_half;
    }
    else
        prev_slow->next = second_half;

    return (is_pal);
}
