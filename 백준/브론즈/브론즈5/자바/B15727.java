package b5;

import java.util.Scanner;

/** 15727번 조별과제를 하려는데 */
public class B15727 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		double n = sc.nextDouble();
		
		System.out.println((int)Math.ceil(n/5));
		
		sc.close();
	}
}
