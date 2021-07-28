package b5;

import java.util.Scanner;

/** 꼬마 정민 : https://www.acmicpc.net/problem/11382 */
public class Jungmin {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long a = sc.nextLong(); // 입력의 범위가 1<= ㅁ <= 10^12 이기때문에 long
		long b = sc.nextLong();
		long c = sc.nextLong();
		
		System.out.println(a+b+c);
		
		sc.close();
	}
}
