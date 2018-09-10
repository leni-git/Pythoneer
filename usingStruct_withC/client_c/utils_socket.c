#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

#include  "utils_header.h"

// #include <sys/types.h>

#define BUFF_SIZE 1024

bool socket_connect(int* client_socket){
  *client_socket = socket(AF_INET, SOCK_STREAM, 0);
  if( -1 == *client_socket ) return false;
  else
  {
    struct sockaddr_in socket_addr;
    memset(&socket_addr, 0, sizeof(socket_addr));
    socket_addr.sin_family = AF_INET;
    socket_addr.sin_port = htons(4000);
    socket_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if(connect(*client_socket, (struct sockaddr*)&socket_addr, sizeof(socket_addr))) return true;
  }
  return false;
}

bool socket_write(int *client_socket, char* text){
  printf("text: %s\n", text);
  printf("len: %ld\n", strlen(text)+1);
  if(write(*client_socket, text, strlen(text)+1)) return true;
  else return false;
}

/*
const는 구조체가 수정되는 것을 막아준다.
구조체가 큰 경우 구조체를 복사해서 넘기는 경우는 성능의 저하를 불러 일으킬 수도 있다.
*/
bool socket_write_struct(int *client_socket, STRUCT_VALUE const *value){
  printf("sizeof value: %ld\n", sizeof(*value));
  printf("sizeof string: %ld\n", sizeof(value->string_value));
  printf("strcut value: %d\n", value->int_value);
  printf("strcut string: %s\n", value->string_value);
  if(write(*client_socket, value, sizeof(*value))) return true;
  else return false;
}

bool socket_read(int *client_socket){
  char buffer[BUFF_SIZE];
  if(read(*client_socket, buffer, BUFF_SIZE+5)){
    printf("server text: %s\n", buffer);
    return true;
  }
  else return false;
}

bool socket_close(int *client_socket){
  if(close(*client_socket)) return true;
  else return false;
}
