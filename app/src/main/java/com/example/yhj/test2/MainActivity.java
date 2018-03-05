package com.example.yhj.test2;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.Toast;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
public class MainActivity extends FragmentActivity{
//startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse("인터넷주소")));
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        //도서관 웹페이지 클릭 버튼 부분
            Button library = (Button) findViewById(R.id.library);
            library.setOnClickListener(new Button.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://library.kunsan.ac.kr"));
                    startActivity(intent);
                }
            });
        //버스 시간표 클릭 부분
        Button bus = (Button) findViewById(R.id.bus_table);
        bus.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent myintent=new Intent(MainActivity.this, testmainactivity.class);
                startActivity(myintent);
            }
        });

        //학식 클릭 부분
        Button school_food = (Button) findViewById(R.id.food_table);
        school_food.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent myintent=new Intent(MainActivity.this, school_restaurant.class);
                startActivity(myintent);
            }
        });
        //기숙사 식당 클릭 부분
        Button domi_food = (Button) findViewById(R.id.domi_res);
        domi_food.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent myintent=new Intent(MainActivity.this, domitory_food.class);
                startActivity(myintent);
            }
        });


}
}

