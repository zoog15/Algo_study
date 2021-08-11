package b3;

import java.util.Scanner;

/** 2884번 알람 시계 */
public class B2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int m = sc.nextInt();
		
		if(m<45) {
			m += 15;
			h -= 1;
		} else
			m -= 45;
		
		if(h<0)
			h += 24;
			
		System.out.println(h+" "+m);
		sc.close();
	}
}
