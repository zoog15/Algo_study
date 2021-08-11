package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2739번 구구단 */
public class B2739 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		for(int i = 1; i <= 9; i++) {
			System.out.println(n+" * "+i+" = "+(i*n));
		}
	}
}