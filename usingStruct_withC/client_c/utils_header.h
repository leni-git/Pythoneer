#ifndef UTILS_HEADER
#define UTILS_HEADER

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct{
  int int_value;
  unsigned char string_value[20];
} STRUCT_VALUE;

bool socket_connect(int* client_socket);
bool socket_write(int* client_socket, char* text);
bool socket_write_struct(int *client_socket, STRUCT_VALUE const *value);
bool socket_read(int* client_socket);
bool socket_close(int* client_socket);

#endif
