/**
 * Payal Patel
 * Project Onboarding Weekly Coding Challenges, Week of March 9, 2022
 **/



public class codingChallenge{
 
public static void main(String args[]){
 
    long evenSum=0;
    long fibo1=1, fibo2=1, fibonacci=1;
    
    for(long i= 3; i<= 150; i++){
        if(fibonacci>=4000000)
            break;
        
        fibonacci = fibo1 + fibo2;
        fibo1 = fibo2;
        fibo2 = fibonacci;
    
        if(fibonacci%2==0){
            evenSum=evenSum+fibonacci;
        }
    
    } 
    System.out.println(evenSum);
    }
 
}