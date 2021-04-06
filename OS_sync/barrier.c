#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "common_threads.h"

// If done correctly, each child should print their "before" message
// before either prints their "after" message. Test by adding sleep(1)
// calls in various locations.

// You likely need two semaphores to do this correctly, and some
// other integers to track things.

typedef struct __barrier_t {
    // add semaphores and other information here
    int THREADS_NUM, threads_count;
    sem_t start_lock, finish_lock;
} barrier_t;


// the single barrier we are using for this program
barrier_t b;

void barrier_init(barrier_t *b, int num_threads) {
    // initialization code goes here
    b->THREADS_NUM = num_threads;
    b->threads_count = 0;
    Sem_init( &(b->start_lock), 1);
    Sem_init (&(b->finish_lock), 1);
}

void barrier(barrier_t *b) {
    // barrier code goes here
    sem_wait(&(b->start_lock));
    b->threads_count++;
    sem_post(&(b->start_lock));
    
    while (b->threads_count != b->THREADS_NUM) {
        sem_wait(&(b->finish_lock));
    }
    sem_post(&(b->finish_lock));
}

//
// XXX: don't change below here (just run it!)
//
typedef struct __tinfo_t {
    int thread_id;
} tinfo_t;

void *child(void *arg) {
    tinfo_t *t = (tinfo_t *) arg;
    
    /* sleep randomly [0,2] seconds, should the randdom number
     * generator be seeded with a diff seed in each thread so
     * that the random numbers would not be the same sequence
     * in every thread, not sure? I think no, since when testing
     * it seemed to be the case that the program "stopped", that
     * is the barrier was up and threads were sleeping in different
     * orders. */
    sleep(rand() % 3);
    printf("child %d: before\n", t->thread_id);
    sleep(rand() % 1);
    barrier(&b);
    printf("child %d: after\n", t->thread_id);
    return NULL;
}


// run with a single argument indicating the number of 
// threads you wish to create (1 or more)
int main(int argc, char *argv[]) {
    assert(argc == 2);
    int num_threads = atoi(argv[1]);
    assert(num_threads > 0);

    pthread_t p[num_threads];
    tinfo_t t[num_threads];

    printf("parent: begin\n");
    barrier_init(&b, num_threads);
    
    int i;
    for (i = 0; i < num_threads; i++) {
	t[i].thread_id = i;
	Pthread_create(&p[i], NULL, child, &t[i]);
    }

    for (i = 0; i < num_threads; i++) 
	Pthread_join(p[i], NULL);

    printf("parent: end\n");
    return 0;
}

