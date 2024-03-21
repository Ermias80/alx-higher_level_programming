#include <stddef.h>
#ifndef LISTS_H
#define LISTS_H
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

#endif /* LISTS_H */        
