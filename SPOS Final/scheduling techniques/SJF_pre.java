import java.util.*;              //preemptive
 
class SJF_pre{
	public static void main (String args[])
	{
		Scanner sc =new Scanner(System.in);
		System.out.println ("enter no of process:");
		int n= sc.nextInt();
		int process_no[] = new int[n]; 
		int arrival_time[] = new int[n]; 
		int burst_time[] = new int[n]; 
		int ct[] = new int[n]; 
		int ta[] = new int[n];
		int wt[] = new int[n];  
		int f[] = new int[n];  
		int k[]= new int[n];   
	    int i, st=0, tot=0;
	    float avgwt=0, avgta=0;
 
	    for (i=0;i<n;i++)
	    {
	    	process_no[i]= i+1;
	    	System.out.println ("enter process " +(i+1)+ " arrival time:");
	    	arrival_time[i]= sc.nextInt();
	    	System.out.println("enter process " +(i+1)+ " burst time:");
	    	burst_time[i]= sc.nextInt();
	    	k[i]= burst_time[i];
	    	f[i]= 0;
	    }
		
	    
	    while(true){
	    	int min=99,c=n;
	    	if (tot==n)
			{
	    		break;
			}	
	    	
	    	for ( i=0;i<n;i++)
	    	{
	    		if ((arrival_time[i]<=st) && (f[i]==0) && (burst_time[i]<min))
	    		{	
	    			min=burst_time[i];
	    			c=i;
	    		}
	    	}
	    	if (c==n)
	    		st++;
	    	else
	    	{
	    		burst_time[c]--;
	    		st++;
	    		if (burst_time[c]==0)
	    		{
	    			ct[c]= st;
	    			f[c]=1;
	    			tot++;
	    		}
	    	}
	    }
	    for(i=0;i<n;i++)
	    {
	    	ta[i] = ct[i] - arrival_time[i];
	    	wt[i] = ta[i] - k[i];
	    	avgwt+= wt[i];
	    	avgta+= ta[i];
	    }
	    
	    System.out.println("pid  arrival  burst  complete turn waiting");
	    for(i=0;i<n;i++)
	    {
	    	System.out.println(process_no[i] +"\t"+ arrival_time[i]+"\t"+ k[i] +"\t"+ ct[i] +"\t"+ ta[i] +"\t"+ wt[i]);
	    }
	    
	    System.out.println("\naverage tat is "+ (float)(avgta/n));
	    System.out.println("average wt is "+ (float)(avgwt/n));
	}
}
/*output:
enter no of process:
3
enter process 1 arrival time:
2
enter process 1 burst time:
4
enter process 2 arrival time:
5
enter process 2 burst time:
7
enter process 3 arrival time:
8
enter process 3 burst time:
14
pid  arrival  burst  complete turn waiting
1	   2   	4	  6	    4	     0
2	   5  	7	 13	    8	      1
3	   8	    14	 27	    19     5

average tat is 10.333333
average wt is 2.0
*/