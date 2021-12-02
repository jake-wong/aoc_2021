#include <stdio.h>
#include <string.h>

int main()
{
    FILE* fp;
    int buffSize = 255;
    char buff[buffSize];

    int horizontalPos = 0;
    int depth = 0;

    fp = fopen("input.txt", "r");
    while(fgets(buff, buffSize, (FILE*)fp))
    {
        char cmd[buffSize];
        strcpy(cmd, buff);
        strtok(cmd, " ");

        int cmdLen = strlen(cmd);
        int num = atoi(&buff[cmdLen]);

        if(!strcmp(cmd, "forward"))
            horizontalPos += num;
        else if(!strcmp(cmd, "down"))
            depth += num;
        else if(!strcmp(cmd, "up"))
            depth -= num;
    }
    printf("Horizontal position: %i\nDepth: %i\nAnswer: %i\n", horizontalPos, depth, horizontalPos * depth);

    return 0;
}