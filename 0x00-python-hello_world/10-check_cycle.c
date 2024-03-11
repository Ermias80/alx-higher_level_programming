#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    if (!list)
        return (0);

    do
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return (1);
    } while (slow && fast && fast->next);

    return (0);
}
