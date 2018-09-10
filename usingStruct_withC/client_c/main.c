#include "utils_header.h"
#include <arpa/inet.h>
void main(void){
  int client_socket;
  bool is_succeed;

  // STRUCT_VALUE struct_value = {13, "I am leni"};
  STRUCT_VALUE struct_value;
  struct_value.int_value = 13;
  memset(struct_value.string_value, 0,  sizeof(struct_value.string_value));
  strcpy(struct_value.string_value, "I am Leni\0");
  // printf("%s\n", struct_value.string_value);

  // Create client socket
  is_succeed = socket_connect(&client_socket);
  if(!is_succeed) printf("socket_connect false\n");
  else printf("socket_connect succeed\n");

  printf("\n");

  is_succeed = socket_write(&client_socket, "Nice leni");
  if(!is_succeed) printf("socket_write false\n");
  else printf("socket_write succeed\n");

  printf("\n");

  is_succeed = socket_read(&client_socket);
  if(!is_succeed) printf("socket_read false\n");
  else printf("socket_read succeed\n");

  printf("\n");

  is_succeed = socket_write_struct(&client_socket, &struct_value);
  if(!is_succeed) printf("socket_write_struct false\n");
  else printf("socket_write_struct succeed\n");

  printf("\n");

  is_succeed = socket_read(&client_socket);
  if(!is_succeed) printf("socket_read false\n");
  else printf("socket_read succeed\n");

  printf("\n");

  is_succeed = socket_close(&client_socket);
  if(!is_succeed) printf("socket_close false\n");
  else printf("socket_close succeed\n");
}
