package b5;

import java.util.Scanner;

/** 14928번 아주 큰 수*/
public class B14928 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
//		BigInteger a = sc.nextBigInteger();
//		BigInteger b = BigInteger.valueOf(20000303);
		String N = sc.nextLine();
		int r = 0, MOD = 20000303;

		for (int i = 0; i < N.length(); i++) {
			r = (r * 10 + (N.charAt(i) - '0')) % MOD;
		}

		System.out.println(r);
		
		sc.close();
	}
}
