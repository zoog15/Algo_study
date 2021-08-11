package b5;

import java.util.Scanner;

/** 14652번 나는 행복합니다~ */
public class B14652 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		
		System.out.printf("%d %d",(k/m),(k%m));
		
		sc.close();
	}
}
