package Beginner_Coder;

import java.util.Scanner;

public class S_1341 {
	static int i,j,k;
	static int n,m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		if(n < m) {
			for(i = n; i<=m; i++) {
				int num = 1;
				for(j=0; j<3; j++) {
					for(k=0; k<3; k++) {
						System.out.printf("%d * %d = %2d   ",i,num,i*num);
						num++;
					}
					System.out.println();
				}
				System.out.println();
			}
		}else {
			for(i = n; i>=m; i--) {
				int num = 1;
				for(j=0; j<3; j++) {
					for(k=0; k<3; k++) {
						System.out.printf("%d * %d = %2d   ",i,num,i*num);
						num++;
					}
					System.out.println();
				}
				System.out.println();
			}
		}
		
		sc.close();
	}

}
