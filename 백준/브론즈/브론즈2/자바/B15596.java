package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 15596번 정수 N개의 합 */
public class B15596 {
	public static long sum(int[] a) {
		long sum = 0;
		
		for(int i = 0; i<a.length;i++) {
			sum += a[i];
		}
		
		return sum;
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		for(int i = 0; i<arr.length;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		long ans = sum(arr);
		
		System.out.println(ans);
	}
}
