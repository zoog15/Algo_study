package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 11021번 A+B -7*/
public class B11021 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(br.readLine());
		int[] arr = new int[tc];
		
		for(int i = 0; i<tc; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			arr[i] = a+b;
		}
		
		for(int i =0; i<arr.length;i++) {
			System.out.printf("Case #%d: %d\n",i+1,arr[i]);
		}
	}
}
