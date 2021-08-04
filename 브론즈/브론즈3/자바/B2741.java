package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2741번 N 찍기 */
public class B2741 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++)
			System.out.println(i + 1);
	}
}
