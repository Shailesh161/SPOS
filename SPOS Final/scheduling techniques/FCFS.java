/*
Arrival Time: The time when a process becomes available for execution.
Burst Time: The time required for a process to complete its execution.
Completion Time: The time at which a process finishes its execution.
 */

import java.util.*;

public class FCFS
{
    public static void main(String args[]) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter no of process: ");
        int n = sc.nextInt();
        int pid[] = new int[n];   // process ids
        int arr[] = new int[n];     // arrival times
        int bt[] = new int[n];     // burst or execution times
        int ct[] = new int[n];     // completion times
        int ta[] = new int[n];     // turn around times
        int wt[] = new int[n];     // waiting times
        int temp;
        float avgwt=0,avgta=0;//average wait time and average turn around time

        for(int i = 0; i < n; i++) {
            System.out.println("enter process " + (i+1) + " arrival time: ");
            arr[i] = sc.nextInt();
            System.out.println("enter process " + (i+1) + " brust time: ");
            bt[i] = sc.nextInt();
            pid[i] = i+1;
        }

//sorting according to arrival times

/*Here Bubble Sort algorithm is used to arrange processes in ascending order of arrival times (ar).
If the arrival time of the current process is greater than the next one, their arrival times, burst times (bt), and process IDs 
(pid) are swapped.
This ensures that processes are scheduled in the order they arrive, a First-Come-First-Serve (FCFS) scheduling algorithm. */
        for(int i = 0 ; i <n; i++) 
        {
            for(int  j=0;  j < n-(i+1) ; j++) 
            {
                if( arr[j] > arr[j+1] ) 
                {
                    temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    temp = bt[j];
                    bt[j] = bt[j+1];
                    bt[j+1] = temp;
                    temp = pid[j];
                    pid[j] = pid[j+1];
                    pid[j+1] = temp;
                }
            }
        }
// finding completion times
        for(int  i = 0 ; i < n; i++)
        {
            if( i == 0)
            {
                ct[i] = arr[i] + bt[i];
            } 
            else 
            {
                if( arr[i] > ct[i-1]) 
                {
                    ct[i] = arr[i] + bt[i];
                }
                else
                {
                    ct[i] = ct[i-1] + bt[i];
                }    
            }
            ta[i] = ct[i] - arr[i] ;              
            // turnaround time= completion time- arrival time
            wt[i] = ta[i] - bt[i] ;              // waiting time= turnaround time- burst time
            avgwt += wt[i] ;                    // total waiting time
            avgta += ta[i] ;                   // total turnaround time
        }
        System.out.println("\npid  arrival  burst  complete turn waiting");
        for(int  i = 0 ; i< n;  i++)
        {
            System.out.println(pid[i] + "  \t " + arr[i] + "\t" + bt[i] + "\t" + ct[i] + "\t" + ta[i] + "\t"  + wt[i] ) ;
        }
        
        System.out.println("\nAverage waiting time using FCFS: "+ (avgwt/n));     // printing average waiting time.
        System.out.println("Average turnaround time using FCFS:"+(avgta/n));    // printing average turnaround time.
        sc.close();
    }
}



//SAMPLE OUTPUT

/* 
enter no of process: 
3
enter process 1 arrival time: 
0
enter process 1 brust time: 
9
enter process 2 arrival time: 
1
enter process 2 brust time: 
4
enter process 3 arrival time: 
2
enter process 3 brust time:
9

pid  arrival  brust  complete turn waiting
1        0      9       9       9       0
2        1      4       13      12      8
3        2      9       22      20      11

average waiting time: 6.3333335
average turnaround time:13.666667
 */