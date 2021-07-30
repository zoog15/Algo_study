package b5;

import java.util.Scanner;

/** 21300번 Bottle Return */
public class B21300 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		int e = sc.nextInt();
		int f = sc.nextInt();
		
		System.out.println(5*(a+b+c+d+e+f));
		sc.close();
	}
}
