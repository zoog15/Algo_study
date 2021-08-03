package b4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 9498번 : 시험 성적 */
public interface B9498 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(in.readLine());
		
		if(n>=90) System.out.println("A");
		else if(n>=80) System.out.println("B");
		else if(n>=70) System.out.println("C");
		else if(n>=60) System.out.println("D");
		else System.out.println("F");
	}
}
