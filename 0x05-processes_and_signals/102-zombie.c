#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
/**
 * create_zombie_processes -  creates 5 zombie processes.
 * @num_zombies: number of zombies to be made
 */
void create_zombie_processes(int num_zombies);

void create_zombie_processes(int num_zombies)
{
	int i;
	pid_t pid;

	for (i = 0; i < num_zombies; ++i)
	{
		pid = fork();

		if (pid < 0)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			/* This is the child process */
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

	/* Parent process waits for a while to allow zombies to be created */
	sleep(10);
}

/**
 * main - Entry point
 * Return: 0 for success
 */

int main(void)
{
	int num_zombies = 5;

	create_zombie_processes(num_zombies);

	/* The parent process continues execution */
	/* You can add more code here if needed */

	return (0);
}
