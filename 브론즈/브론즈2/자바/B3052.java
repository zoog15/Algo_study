package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/** 3052번 나머지 */
public class B3052 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[10];
		int cnt = 1;
		
		for(int i = 0; i<10; i++) {
			int n = Integer.parseInt(br.readLine());
			int mod = n % 42;
			arr[i] = mod;
		}
		
		Arrays.sort(arr);  // 배열 정렬
		
		for(int i = 0; i<9; i++) {
			if(arr[i] != arr[i+1]) {
				cnt += 1;
				continue;
			}
		}
		
		System.out.println(cnt);
	}
}
