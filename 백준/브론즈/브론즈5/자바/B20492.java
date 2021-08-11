package b5;

import java.util.Scanner;

/** 20492번 세금 */
public class B20492 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		double a = 0.78 * n;
		double b = ((1-(0.2*0.22))*n);
		
		System.out.println((int)a + " " + (int)b);
		
		sc.close();
	}
}
