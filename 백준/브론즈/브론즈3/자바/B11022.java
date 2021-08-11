package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 11022번 A+B -8 */
public class B11022 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int tc = Integer.parseInt(br.readLine());
		int[] arr = new int[tc];
		int[] arra = new int[tc];
		int[] arrb = new int[tc];

		for (int i = 0; i < tc; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			arra[i] = a;
			arrb[i] = b;
			arr[i] = a + b;
		}

		for (int i = 0; i < arr.length; i++) {
			System.out.printf("Case #%d: %d + %d = %d\n", i + 1,arra[i],arrb[i], arr[i]);
		}
	}
}
