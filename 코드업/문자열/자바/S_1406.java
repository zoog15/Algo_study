package String;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S_1406 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s = br.readLine();
		
		if(s.equals("love")){
			System.out.println("I "+ s + " you.");
		}
	}
}
