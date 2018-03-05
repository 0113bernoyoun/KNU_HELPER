package com.example.yhj.test2;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.widget.ImageView;

import com.squareup.picasso.Picasso;

/**
 * Created by YHJ on 2017-09-25.
 */

public class testmainactivity extends FragmentActivity {
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_test);

        ImageView imageview = (ImageView)findViewById(R.id.imageView2);
       // Picasso.with(this).load(R.drawable.bustimetable).fit().into(imageview);
        imageview.setImageResource(R.drawable.bustimetable);
    }
}
