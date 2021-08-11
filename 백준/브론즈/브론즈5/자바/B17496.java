package b5;

import java.util.Scanner;

/** 17496번 스타후르츠 */
public class B17496 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int t = sc.nextInt();
		int c = sc.nextInt();
		int p = sc.nextInt();
		int day = 0;
		
		if(n%t == 0) { day = n/t-1; }
		else { day = n/t; }
		
		System.out.println(day*c*p);
	}
}
