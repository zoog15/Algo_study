package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2438번 별 찍기 1 */
public class B2438 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(in.readLine());
		
		for(int i = 0; i< n ; i++) {
			for(int j = 0; j < i+1; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
