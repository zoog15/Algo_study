package String;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S_1733 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		if(s.equals("IOI")) {
			System.out.println("IOI is the International Olympiad in Informatics.");
		}
		else
			System.out.println("I don't care.");
	}
}
