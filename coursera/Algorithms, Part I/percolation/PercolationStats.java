public class PercolationStats {
	Percolation p;
	double[] resultList;
	
	
	// perform T independent computational experiments on an N-by-N grid
	public PercolationStats(int N, int T){
		resultList = new double[T];
		
//		stimulation of T times  
		for(int m=0;m<T;m++){

			p = new Percolation(N);
			
			for(int k=0;k<N*N;k++){
				
				   int index = (int)(Math.random()*p.container.size());
				   p.wOpen[index] = true;
				   
				   int convert = (Integer)p.container.get(index); 
				   int i = convert / N;
				   int j = convert - i * N;
				   p.container.remove(index);
				   
				   p.open(i, j);
				   if(i==N-1){
					   if(p.isFull(i, j)){
						   resultList[m] = (double)p.proOpen / (N*N);
						   break;
					   }
				   }
			}
		}
	}
	
	// sample mean of percolation threshold 
    public double mean(){
    	double sum =0;
    	for(int i=0;i<resultList.length;i++){
    		sum += resultList[i];
    	}
    	return sum/(resultList.length+1);
    }
	
	// sample standard deviation of percolation threshold 
    public double stddev(){
    	double sum =0;
    	double squSum = 0;
    	for(int i=0;i<resultList.length;i++){
    		sum += resultList[i];
    	}
    	double mean = sum/(resultList.length+1);
    	
    	for(int i=0;i<resultList.length;i++){
    		squSum += ( resultList[i] - mean ) * ( resultList[i] - mean );
    	}
    	return (squSum/resultList.length); 
    }
	
	// returns lower bound of the 95% confidence interval
    public double confidenceLo(){
    	double sum =0;
    	double squSum = 0;
    	for(int i=0;i<resultList.length;i++){
    		sum += resultList[i];
    	}
    	double mean = sum/(resultList.length+1);
    	
    	for(int i=0;i<resultList.length;i++){
    		squSum += ( resultList[i] - mean ) * ( resultList[i] - mean );
    	}
    	double sttdev = squSum/resultList.length;
    	return mean - 1.96 * sttdev / Math.sqrt(resultList.length+1);
    }
   
	// returns upper bound of the 95% confidence interval
    public double confidenceHi(){
    	double sum =0;
    	double squSum = 0;
    	for(int i=0;i<resultList.length;i++){
    		sum += resultList[i];
    	}
    	double mean = sum/(resultList.length+1);
    	
    	for(int i=0;i<resultList.length;i++){
    		squSum += ( resultList[i] - mean ) * ( resultList[i] - mean );
    	}
    	double sttdev = squSum/resultList.length;
    	return  mean + 1.96 * sttdev / Math.sqrt(resultList.length+1);
    }
   
	// test client, described below
    public static void main(String[] args){
    	PercolationStats exper = new PercolationStats(2, 10000);
    	System.out.print("mean: "+exper.mean()+" stddev"+exper.stddev());
	}
}