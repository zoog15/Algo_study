package b4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2753번 윤년 */
public class B2753 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int year = Integer.parseInt(in.readLine());
		
		if((year%4==0 && year%400==0) || (year%4==0 && year%100 != 0))
			System.out.println("1");
		else
			System.out.println("0");
	}
}
