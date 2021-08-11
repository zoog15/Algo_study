package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2742번 기찍 N */
public class B2742 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = n; i>0; i--)
			System.out.println(i);
	}
}
