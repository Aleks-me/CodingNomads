package labs_examples.input_output.examples;

// Read a string from console using a BufferedReader.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class ReadLines {
    public static void main(String args[])
            throws IOException
    {
        // create a BufferedReader using System.in
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String str;

        System.out.println("Enter lines of text.");
        System.out.println("Enter 'stop' to quit.");
        do {
            str = br.readLine();
            System.out.println(str);
        } while(!str.equals("stop"));
    }
}
