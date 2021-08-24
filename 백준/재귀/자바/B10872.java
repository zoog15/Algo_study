package algo.recur;

import java.util.Scanner;

/** 10872번 팩토리얼 */
public class B10872 {
	public static int factorial(int n) {
		if(n == 0 || n == 1) return 1;
		return n * factorial(n-1);
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		System.out.println(factorial(n));
		sc.close();
	}
}
