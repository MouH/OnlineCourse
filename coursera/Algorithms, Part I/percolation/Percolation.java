import java.util.ArrayList;

public class Percolation {
	
	WeightedQuickUnionUF w;
	boolean[] wOpen; 
	int size;
	int proOpen = 0;
	ArrayList container;
	
	// create N-by-N grid, with all sites blocked
    public Percolation(int N){
       w = new WeightedQuickUnionUF(N*N);
	   wOpen = new boolean[N*N];
	   size = N;
	   container = new ArrayList(N*N);
	   
//	   initialize the model
	   for(int k=0;k<N*N;k++){
	       wOpen[k] = false;
	       container.add(k);
	   }
	   

    }
   
    // open site (row i, column j) if it is not already
    public void open(int i, int j){

    	int convert = i * size + j;
    	
        if(!isOpen(i,j)){
        	wOpen[convert] =  true; 
        	proOpen ++;
        	
        	if(i>0){
        		if(wOpen[convert-size]){
        			w.union(convert, convert-size);
        		}
        	}
        	if(i<size-1){
        		if(wOpen[convert+size]){
        			w.union(convert, convert+size);
        		}
        	}
        	if(j<size-1){
        		if(wOpen[convert+1]){
        			w.union(convert, convert+1);
        		}
        	}
        	if(j>0){
        		if(wOpen[convert-1]){
        			w.union(convert, convert-1);
        		}
        	}      	
        }
    }
   
   // is site (row i, column j) open?
    public boolean isOpen(int i, int j){
    	int convert = i * size + j;
    	return wOpen[convert];
    }
   
    // is site (row i, column j) full?
    public boolean isFull(int i, int j){
    	for(int k=0;k<size;k++){
    		if(w.connected(k, i*size+j)){
    			return true;
    		}
    	}
    	return false;
    }
   
    // does the system percolate?
    public boolean percolates(){
    	for(int l = size*(size-1);l<size*size;l++){
    		for(int k=0;k<size;k++){
        		if(w.connected(k, l)){
        			return true;   			
    		    }
    		}
    	}
    	return false;
    }
}