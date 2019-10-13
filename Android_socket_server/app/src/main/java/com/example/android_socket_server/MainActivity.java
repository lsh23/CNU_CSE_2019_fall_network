package com.example.android_socket_server;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Notification;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class MainActivity extends AppCompatActivity {

    private ServerSocket serverSocket;
    private Socket client_socket;
    private EditText port;
    private EditText msg;
    private TextView chattings;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        port = (EditText) findViewById(R.id.port);
        msg = (EditText) findViewById(R.id.msg);
        chattings = (TextView) findViewById(R.id.chattings);

        new Thread(new ServerThread()).start();
        new Thread(new recvThread()).start();
        new Thread(new sendThread()).start();
    }




    public void SendClient(View view) {

    }

    public void ServerOpen(View view) {

    }


    private String getLocalIpAddress() throws UnknownHostException {

    }


    private class recvThread implements Runnable {
        @Override
        public void run() {

        }
    }

    private class sendThread implements Runnable {
        @Override
        public void run() {

        }
    }

    private class ServerThread implements Runnable {
        @Override
        public void run() {

        }
    }
}
