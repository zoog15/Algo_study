package b5;

import java.math.BigInteger;
import java.util.Scanner;

/** 13277번 큰 수의 곱셈 */
public class BigMul {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		
		System.out.println(a.multiply(b));
		
		
		sc.close();
	}
}
