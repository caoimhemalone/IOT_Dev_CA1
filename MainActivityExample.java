package com.example.caoimhe.ca1app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Switch;
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
    private TextView view;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Button button = (Button) findViewById(R.id.button);

        //button.setOnClickListener(this);
//
//        Switch ledswitch1 = (Switch) findViewById(R.id.led1Switch);
//        ledswitch1.setOnClickListener(this);
//        Switch ledswitch2 = (Switch) findViewById(R.id.led2Switch);
//        ledswitch2.setOnClickListener(this);
//        Switch ledswitch3 = (Switch) findViewById(R.id.led3Switch);
//        ledswitch3.setOnClickListener(this);
        Button led1btn = (Button) findViewById(R.id.led1BTN);
        led1btn.setOnClickListener(this);
        Button led2btn = (Button) findViewById(R.id.led2BTN);
        led2btn.setOnClickListener(this);
        Button led3btn = (Button) findViewById(R.id.led3BTN);
        led3btn.setOnClickListener(this);
        Button cambtn = (Button) findViewById(R.id.camBTN);
        cambtn.setOnClickListener(this);
//        Button startbtn = (Button) findViewById(R.id.startBTN);
//        startbtn.setOnClickListener(this);
        
        view = (TextView) findViewById(R.id.messageTV);

        mQueue = CustomQueue.getInstance(this.getApplicationContext())
                .getRequestQueue();
    }

    @Override
    public void onClick(View view) {
        String url;
        switch (view.getId()){
//            case R.id.startBTN:
////                JSONObject data0 = new JSONObject();
////                try {
////                    data0.put("start", "true");
////                } catch (JSONException e){
////                    e.printStackTrace();
////                }
//
//                url = "https://dweet.io/dweet/for/caoimhe?publish=true";
//                final CustomJSONRequest jsonRequest0 = new CustomJSONRequest(Request.Method.GET, url,
//                        new JSONObject(), this, this);
//                jsonRequest0.setTag("test");
//                mQueue.add(jsonRequest0);
//                break;

            case R.id.led1BTN:
//                JSONObject data = new JSONObject();
//                try {
//                    data.put("start", "true");
//                } catch (JSONException e){
//                    e.printStackTrace();
//                }

                url = "https://dweet.io/dweet/for/caoimhe?publish=led1";
                final CustomJSONRequest jsonRequest = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest.setTag("test");
                mQueue.add(jsonRequest);
                break;

            case R.id.led2BTN:
//                JSONObject data2 = new JSONObject();
//                try {
//                    data2.put("start", "true");
//                } catch (JSONException e){
//                    e.printStackTrace();
//                }

                url = "https://dweet.io/dweet/for/caoimhe?publish=led2";
                final CustomJSONRequest jsonRequest2 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest2.setTag("test");
                mQueue.add(jsonRequest2);
                break;

            case R.id.led3BTN:
//                JSONObject data3 = new JSONObject();
//                try {
//                    data3.put("publish", "led3");
//                } catch (JSONException e){
//                    e.printStackTrace();
//                }

                url = "https://dweet.io/dweet/for/caoimhe?publish=led3";
                final CustomJSONRequest jsonRequest3 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest3.setTag("test");
                mQueue.add(jsonRequest3);
                break;

            case R.id.camBTN:
//                JSONObject data4 = new JSONObject();
//                try {
//                    data4.put("start", "true");
//                } catch (JSONException e){
//                    e.printStackTrace();
//                }

                url = "https://dweet.io/dweet/for/caoimhe?publish=cam";
                final CustomJSONRequest jsonRequest4 = new CustomJSONRequest(Request.Method.GET, url,
                        new JSONObject(), this, this);
                jsonRequest4.setTag("test");
                mQueue.add(jsonRequest4);
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
