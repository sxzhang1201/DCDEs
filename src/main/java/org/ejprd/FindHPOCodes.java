package org.ejprd;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.util.Scanner;

public class FindHPOCodes
{
    public static final String LE = "\n"; // using Unix line endings is the safer option

    private File input;
    private File output;

    public FindHPOCodes(File input, File output)
    {
        this.input = input;
        this.output = output;
    }

    public void start() throws Exception {

        FileWriter fw = new FileWriter(output);
        BufferedWriter bw = new BufferedWriter(fw);

        Scanner s = new Scanner(input);

        while(s.hasNextLine())
        {
            String request = s.nextLine();
            if(request.isEmpty())
            {
                bw.write(LE);
                continue;
            }
            String response = NCC.getHPOterms(request, 100).trim();
            System.out.println("Request: '" + request + "', response: '" + response + "'.");
            bw.write(request + "\t" + response + LE);
            bw.flush();
        }
        bw.close();
    }

}
