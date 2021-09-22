package Beginner_Coder;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S_1402 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int p = Integer.parseInt(st.nextToken());
		int q = Integer.parseInt(st.nextToken()); 
		
		String s = "";
		
		for (int i = 1; i <= p; i++) {
			if (p % i == 0) {
				s += i+" ";
			}
		}
		
		String[] arr = s.split(" ");
		
		if(arr.length < q) System.out.println(0);
		else System.out.println(arr[q-1]);
	}
}
