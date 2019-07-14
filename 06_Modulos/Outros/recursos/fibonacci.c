#include "/usr/include/python3.5m/Python.h"
#include <stdio.h>
#include <stdlib.h>

int fib(int n) {
  if (n < 2)
    return n;
      
  return fib(n - 1) + fib(n - 1);
}

static PyObject* fibonacci(PyObject* self, PyObject* args) {
  int n;
    
  if (!PyArg_ParseTuple(args, "i", &n))
    return NULL;
      
  return Py_BuildValue("i", fib(n));
}

static PyObject* version(PyObject* self) {
  return Py_BuildValue("s", "Versão 1.0");
}

static PyMethodDef myMethods[] = {
  {"fibonacci", fibonacci, METH_VARARGS, "Calculo do numero de Fibonacci"},
  {"version", version, METH_NOARGS, "Retorna a versao"},
  {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initmyModule(void) {
  (void) Py_InitModule("fibonacci", myMethods);
}