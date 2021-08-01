package b5;

import java.util.Scanner;

public class korean2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		char result = s.charAt(0);  // 들어온 String 을 char로 변환
		System.out.println((int)result - 44031);
		
		sc.close();
	}
}
