import java.util.Scanner;
 
class LRU 
{ 
    public static int min(int counter[],int nFrames)
    {
	    int minimum = counter[0];
	    int pos = 0;
	    for(int i=0;i<nFrames;i++) 
	    {
	    	if(minimum > counter[i])
	    	{
	    		minimum=counter[i];
	    		pos=i;
	    	}
    	}
	    return pos;   
    }    
    public static void main(String[] args) 
    {
        Scanner s = new Scanner(System.in);
    	int n,recent = 0,pageFault = 0,nFrames;
    	int pagehits=0;
        
    	System.out.print("Enter the number of pages: ");
      	n = s.nextInt();
    	int pageString[] = new int[n]; 
    	System.out.print("Enter the page reference string: ");
    	for(int i=0;i<n;i++)
        	pageString[i]=s.nextInt();
       
     	System.out.print("\nEnter the number of frames: "); 
        nFrames = s.nextInt();
     	int frames[] = new int[nFrames];
     	int counter[] = new int[nFrames];
    
     	for(int i=0;i<nFrames;i++)
     	{
     		frames[i] = 0; 
        counter[i] = 0;
    	}
     
    	for(int i=0;i<n;i++)
    	{
    		int flag =0;
      	for(int j=0;j<nFrames;j++)
      	{
       		if(frames[j] == pageString[i])
         		{
         			flag=1;
          		counter[j] = recent++;
          		pagehits++;
         			break;
         		}
      	}
         
      	if(flag == 0)
      	{
          		for(int j=0;j<nFrames;j++)
          		{
          			if(frames[j] == 0)
            		{
            			frames[j] = pageString[i];
            			counter[j] = recent++;
            			flag=1;
            			pageFault++;
            			break;
            		}   
          		}
      	}
      	if(flag == 0)
      	{
      		int PositionToreplace = min(counter,nFrames);
      		frames[PositionToreplace] = pageString[i];
      		counter[PositionToreplace] = recent++;
      		pageFault++;
      	}
     		System.out.println();
    		for(int j=0;j<nFrames;j++)
    		{
       		System.out.print(frames[j]+" ");
    		}
     	}      	
    	System.out.println("Page Fault: "+pageFault);
    	System.out.println("Page Hits: "+pagehits);
    	System.out.println("Hit Ratio: "+(float)(pagehits)/n);
		s.close();
    }
}