package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2439번 별 찍기 2 */
public class B2439 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(in.readLine());
		
		for(int i = 0;i<n;i++) {
			for(int j = n-1; j>i; j--) {
				System.out.print(" ");
			}
			for(int k = 0; k<i+1;k++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
