package b2;

import java.util.Scanner;

/** 1152번 단어의 개수 */
public class B1152 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine(); 
		String a = s.trim();
		String[] x = a.split(" ");
		
		if(x[0].equals("")) 
			System.out.println("0");
		else
			System.out.println(x.length);
		
		sc.close();
	}
}
