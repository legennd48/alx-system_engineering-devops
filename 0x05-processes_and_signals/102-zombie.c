#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - create infinite sleep loop
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: infinite_while zombies
 */
int main(void)
{
	pid_t zombie;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", zombie);
		}
	}
	return (infinite_while());
}
