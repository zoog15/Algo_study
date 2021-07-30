package b5;

import java.util.Scanner;

/** 18301번 Rats */
public class B18301 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		System.out.println((a+1)*(b+1)/(c+1)-1);
		sc.close();
	}
}
