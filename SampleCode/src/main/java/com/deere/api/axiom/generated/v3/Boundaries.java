/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.deere.api.axiom.generated.v3;

import java.io.FileWriter;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.util.List;
import java.lang.String;

/**
 *
 * @author Kurtis Reid
 */
//create boundry class
public class Boundaries extends Resource {
    
    private int feild;
    String name = "long.txt";
    //private long boundary1;
    //double lat[];
    //double longitude[];
    //private int numOfpoints;
    private List<Multipolygon> multipolygon;
   // File file = new File("latit.txt");
   // File file2 = new File("long.txt");
   // FileWriter writer = new FileWriter(file, true);
   // FileWriter writer2 = new FileWriter(file, true);
    //PrintWriter toFile = new PrintWriter(writer);
    //PrintWriter toFile2 = new PrintWriter(writer2);
    
    
    //XStream xstream = new XStream(new StaxDriver());
    public int getFeild()
    {
        return feild;
    }

    public void setFeild(int feild) {
        this.feild = feild;
    }

    public List<Multipolygon> getMultipolygon() {
        return multipolygon;
    }

    //points = new long[1][1];
    //private boolean passable;
    //private boolean exterior; // false = inside feild, true = edge of feild
    // multipolygon object
    //ring objcet which contains a list of points
    //
    public void toxml(){
        String xml = multipolygon.toString();
      //  xml.toXMLString();
    }
    public void print_long()
    {
        
        
        System.out.println(multipolygon.get(0).getRings().get(0).getType());
        System.out.println(multipolygon.get(0).getRings().get(0).getPassable());
        System.out.println(multipolygon.get(0).getRings().get(0).getPoints().get(0));
        System.out.println(multipolygon.get(0).getRings().get(0).getPoints().get(2));
    }
    public void setMultipolygon(List<Multipolygon> multipolygon) {
        this.multipolygon = multipolygon;
    }

    public int getfield() {
        return feild;
    }
    
   
  
}