#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: Pointer to a Python list object
 *
 * Description: This function prints the size of a Python list, the amount of
 * memory allocated for it, and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
    if (p == NULL || !PyList_Check(p))
    {
        printf("  [ERROR] Invalid Python list\n");
        return;
    }

    Py_ssize_t size = Py_SIZE(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);
    for (Py_ssize_t elem = 0; elem < size; elem++)
        printf("Element %ld: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}
