package b5;

import java.util.Scanner;

/** 17256번 달달함이 넘쳐흘러 */
public class B17256 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int ax = sc.nextInt();
		int ay = sc.nextInt();
		int az = sc.nextInt();
		
		int cx = sc.nextInt();
		int cy = sc.nextInt();
		int cz = sc.nextInt();
		
		System.out.println((cx-az)+" " +  (cy/ay) + " " + (cz-ax));
		
		sc.close();
	}
}
