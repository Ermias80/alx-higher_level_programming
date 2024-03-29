#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * print_python_list_info -  function that prints some basic
 *							info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
    int elem;

    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (elem = 0; elem < Py_SIZE(p); elem++)
    {
        PyObject *item = PyList_GetItem(p, elem);
        printf("Element %d: %s\n", elem, Py_TYPE(item)->tp_name);
    }
}
