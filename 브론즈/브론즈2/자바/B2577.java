package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2577번 숫자의 개수 */
public class B2577 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		int c = Integer.parseInt(br.readLine());
		
		int mul = a*b*c;
		int[] arr = new int[10];
		
		
		while(true) {
			if(mul == 0) break;
			
			int mod = mul % 10;
			arr[mod]++;
			mul/=10;
		}
		
		for(int i = 0; i<arr.length;i++) {
			System.out.println(arr[i]);
		}
	}
}
