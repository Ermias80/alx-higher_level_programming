#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid Python list object\n");
        return;
    }

    Py_ssize_t length = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", length);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Python bytes object\n");
        return;
    }
    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
