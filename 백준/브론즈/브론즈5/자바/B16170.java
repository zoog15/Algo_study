package b5;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

/** 오늘의 날짜는? */
public class B16170 {
	public static void main(String[] args) {
		TimeZone time;
		Date date = new Date();
		
		// 날짜를 표현할 Format 설정
		DateFormat yf = new SimpleDateFormat("yyyy");
		DateFormat mf = new SimpleDateFormat("MM");
		DateFormat df = new SimpleDateFormat("dd");
		
		// getTimeZone에 아무값도 없으면 세계표준시로 초기화됨
		// setTimeZone 초기화는 아무곳에나 해도 상관없는듯
		time = TimeZone.getTimeZone("");
		yf.setTimeZone(time);
		System.out.format("%s\n",yf.format(date));
		System.out.format("%s\n",mf.format(date));
		System.out.format("%s",df.format(date));
	}
}
