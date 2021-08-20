import java.util.Scanner;

public class S_1291 {
	static int i, j;
	static int n, m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			n = sc.nextInt();
			m = sc.nextInt();
			
			if((2<=n)&&(n<=9) && ((2<=m)&&(m<=9))) break;
			else System.out.println("INPUT ERROR!");
		}

		for(i=1; i<=9; i++) {
			if(n < m) {
				for(j = n; j<=m; j++) {
					System.out.printf("%d * %d = %2d   ",j,i,j*i);
				}
			}else {
				for(j = n; j>=m; j--) {
					System.out.printf("%d * %d = %2d   ",j,i,j*i);
				}
			}
			System.out.println();
		}
		
		sc.close();
	}
}
