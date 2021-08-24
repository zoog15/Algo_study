package recur;

import java.util.Scanner;

/** 1901번 1부터 n까지 출력하기 */
public class S_1901 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		asc_p(n);
		
		sc.close();
	}

	private static int i = 1;
	
	private static void asc_p(int n) {
		if(i==n+1) return;
		System.out.println(i++);
		asc_p(n);
	}
}
