package b5;

import java.math.BigInteger;
import java.util.Scanner;

/** 15740번 A+B -9 */
public class B15740 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		
		System.out.println(a.add(b));
		
		sc.close();
	}
}
