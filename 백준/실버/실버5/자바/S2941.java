package S5;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/** 2941번 크로아티아 알파벳 */
public class S2941 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] cro = {"c=","c-","dz=","d-","lj","nj","s=","z="}; // 크로아티아 알파벳
		
		String s = br.readLine();
		
		for(int i = 0; i < cro.length; i++) {
			s = s.replace(cro[i], "a");
		}
		
		System.out.println(s.length());
	}
}
