package com.example.yhj.test2;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.Image;
import android.support.v4.app.FragmentActivity;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout.LayoutParams;

import uk.co.senab.photoview.PhotoViewAttacher;
public class Main22Activity extends FragmentActivity {
    ImageView m_imageview;
    PhotoViewAttacher mAttacher;
    Context mContext;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main22);

       // Bitmap size= BitmapFactory.decodeResource(getResources(),R.drawable.bustableall);
      //  size=Bitmap.createScaledBitmap(size,700,700,true);
      //  m_imageview.setImageBitmap(size);
/*
     DisplayMetrics metrics=new DisplayMetrics();
        WindowManager windowManager= (WindowManager)getApplicationContext().getSystemService(Context.WINDOW_SERVICE);
        windowManager.getDefaultDisplay().getMetrics(metrics);
        m_imageview=(ImageView)findViewById(R.id.bus_img);
        LayoutParams params=(LayoutParams)m_imageview.getLayoutParams();
        params.width=metrics.widthPixels;
        params.height=metrics.heightPixels;
        m_imageview.setLayoutParams(params);







        mAttacher=new PhotoViewAttacher(m_imageview);

*/


/*
        Button button = (Button) findViewById(R.id.btn_alert);
        button.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {

                DisplayMetrics metrics = new DisplayMetrics();
                WindowManager windowManager = (WindowManager) getApplicationContext()
                        .getSystemService(Context.WINDOW_SERVICE);
                windowManager.getDefaultDisplay().getMetrics(metrics);

                ImageView img = (ImageView) findViewById(R.id.bus_img);
                LayoutParams params = (LayoutParams) img.getLayoutParams();
                params.width = metrics.widthPixels;
                params.height = metrics.heightPixels;

                img.setLayoutParams(params);
            }
        });

*/


    }

}
