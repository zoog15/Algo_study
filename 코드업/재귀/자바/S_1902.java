package recur;

import java.util.Scanner;

public class S_1902 {
	public static void des_p(int n) {
		if(n==0) return;
		System.out.println(n--);
		des_p(n);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		des_p(n);
		
		sc.close();
	}
}
