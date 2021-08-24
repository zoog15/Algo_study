package recur;

import java.util.Scanner;

public class S_1904 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		odd_p(a, b);
	}

	private static void odd_p(int a, int b) {
		if(a == b+1) return;
		if(a%2 == 1) System.out.print(a+" ");
		a++;
		odd_p(a, b);
	}
}
