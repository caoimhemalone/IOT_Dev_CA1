package com.example.caoimhe.ca1app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.example.caoimhe.ca1app.R;

import org.json.JSONException;
import org.json.JSONObject;

// Volley sample code is adapted from a tutorial @ http://www.truiton.com/2015/02/android-volley-example/
// This example is simple and easy to follow, and it is all we need for a simple HTTP request and callback through Volley

public class MainActivity extends AppCompatActivity implements View.OnClickListener, Response.Listener, Response.ErrorListener {

    private RequestQueue mQueue;
    private TextView view, timeSeek;

    int time;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button led1btn = (Button) findViewById(R.id.led1BTN);
        led1btn.setOnClickListener(this);
        Button led2btn = (Button) findViewById(R.id.led2BTN);
        led2btn.setOnClickListener(this);
        Button led3btn = (Button) findViewById(R.id.led3BTN);
        led3btn.setOnClickListener(this);
        Button cambtn = (Button) findViewById(R.id.camBTN);
        cambtn.setOnClickListener(this);
        TextView tempTV = (TextView) findViewById(R.id.temp);

        TextView humTV = (TextView) findViewById(R.id.hum);

        
        view = (TextView) findViewById(R.id.messageTV);

        mQueue = CustomQueue.getInstance(this.getApplicationContext())
                .getRequestQueue();

        timeSeek = (TextView) findViewById(R.id.time);
        SeekBar seekbar = (SeekBar) findViewById(R.id.seekBar);

        time = seekbar.getProgress();
        timeSeek.setText(String.valueOf(time));

        seekbar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                time = seekBar.getProgress();
                timeSeek.setText(String.valueOf(time));
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }

    @Override
    public void onClick(View view) {
        String url;
        switch (view.getId()){
            case R.id.led1BTN:

                url = "https://dweet.io/dweet/for/caoimhe?publish=led1&time="+time;
                final CustomJSONRequest jsonRequest = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest.setTag("test");
                mQueue.add(jsonRequest);
                break;

            case R.id.led2BTN:

                url = "https://dweet.io/dweet/for/caoimhe?publish=led2&time="+time;
                final CustomJSONRequest jsonRequest2 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest2.setTag("test");
                mQueue.add(jsonRequest2);
                break;

            case R.id.led3BTN:

                url = "https://dweet.io/dweet/for/caoimhe?publish=led3&time="+time;
                final CustomJSONRequest jsonRequest3 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest3.setTag("test");
                mQueue.add(jsonRequest3);
                break;

            case R.id.camBTN:

                url = "https://dweet.io/dweet/for/caoimhe?publish=cam&time="+time;
                final CustomJSONRequest jsonRequest4 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest4.setTag("test");
                mQueue.add(jsonRequest4);
                break;

            case R.id.temp:

                url = "https://dweet.io/dweet/for/caoimhe?publish=temp";
                final CustomJSONRequest jsonRequest5 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest5.setTag("test");
                mQueue.add(jsonRequest5);
                break;

            case R.id.hum:

                url = "https://dweet.io/dweet/for/caoimhe?publish=hum";
                final CustomJSONRequest jsonRequest6 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest6.setTag("test");
                mQueue.add(jsonRequest6);
                break;
        }
    }

    @Override
    public void onErrorResponse(VolleyError error) {

    }

    @Override
    public void onResponse(Object response) {
        Toast.makeText(getApplicationContext(),response.toString(), Toast.LENGTH_LONG).show();
        view.setText(response.toString());
    }
}
