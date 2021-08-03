package b4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2588번 곱셈 */ 
public class B2588 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(in.readLine());
		int b = Integer.parseInt(in.readLine());
		int result = a*b;
		
		while(b != 0) {
			System.out.println((b%10)*a);
			b /= 10;
		}
		System.out.println(result);
	}
}
