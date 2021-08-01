package b5;

import java.util.Scanner;

/** 15964번 : 이상한 기호 */
public class B15964 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong();
		long b = sc.nextLong();
		
		System.out.println((a+b)*(a-b));
		
		sc.close();
	}
}
