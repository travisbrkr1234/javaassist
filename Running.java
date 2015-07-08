import java.util.*;
import java.io.*;

public class Running {
  public static void main(String[] args) throws Exception {
    System.setOut(new PrintStream(new FileOutputStream("Results.txt")));

      try {
        String cmd = "orderquery";
        String line;
        Process p = Runtime.getRuntime().exec("python " + cmd + ".py");
        System.out.println("Running " + cmd);
        System.out.println(" ");
        System.out.println(cmd + "Ran Successfully");

        BufferedReader in = new BufferedReader(
                new InputStreamReader(p.getInputStream()) );
        while ((line = in.readLine()) != null) {
          System.out.println(line);
        }
        in.close();
      }
      catch (Exception e) {
        System.out.println("Hey! You did something exceptionally wrong...");
      }
    }
 }
