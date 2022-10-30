//QUESTION 1
package com.company;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Map<String,Integer> words = new HashMap<String,Integer>();
        countEachWord("C:\\Users\\Priyanshi Tripathi\\Desktop\\JavaWork\\src\\icep.txt",words);
        System.out.println("Word     Frequency");
        System.out.println(words);
        int max = getMaxOccurence(words);
        for (Map.Entry<String, Integer> word: words.entrySet()){
            if(word.getValue() == max){
                System.out.println("The most occurring word=" + word);
            }
        }

    }
    static void countEachWord(String fileName, Map<String, Integer> words) throws FileNotFoundException {
        Scanner file = new Scanner(new File(fileName));
        while (file.hasNext()){
            String word = file.next();
            Integer count = words.get(word);
            if(count != null)
                count++;
            else
                count = 1;
            words.put(word, count);
        }
        file.close();
    }
    static int getMaxOccurence(Map<String, Integer> words){
        int max = 1;
        for(Map.Entry<String,Integer> word: words.entrySet()){
            if(word.getValue() > max){
                max = word.getValue();
            }
        }
        return max;
    }

}

//QUESTION 1.2
package com.company;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Map<String,Integer> words = new HashMap<String,Integer>();
        Map<String,Integer> woord = new HashMap<String,Integer>();
        countEachWord("C:\\Users\\Priyanshi Tripathi\\Desktop\\JavaWork\\src\\happy_sentiment_dictionary.txt",words);
        countEachWord("C:\\Users\\Priyanshi Tripathi\\Desktop\\JavaWork\\src\\sad_sentiment_dictionary.txt",woord);
        System.out.println("PositiveWords     Frequency");
        System.out.println(words);
        System.out.println("NegativeWords    Frequency");
        System.out.println(woord);

    }
    static void countEachWord(String fileName, Map<String, Integer> words) throws FileNotFoundException {
        Scanner file = new Scanner(new File(fileName));
        while (file.hasNext()){
            String word = file.next();
            Integer count = words.get(word);
            if(count != null)
                count++;
            else
                count = 1;
            words.put(word, count);
        }
        file.close();
    }
void countEachWoord(String fileName, Map<String, Integer> woord) throws FileNotFoundException{
    Scanner file = new Scanner(new File(fileName));
    while (file.hasNext()){
        String word = file.next();
        Integer count = woord.get(word);
        if(count != null)
            count++;
        else
            count = 1;
        woord.put(word, count);
    }
    file.close();
}

}
//QUESTION 2
package com.company;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Main {
    public static void main(String[] args)  {
        int n = 5;
        for (int i = 1; i<=n ; i++) {
            for(int j = i; j<=n; j++){
                System.out.print(" ");
            }
            for (int k = 1; k< i; k++) {
                if(i== n || k== 1)
                System.out.print("*");
                else
                    System.out.print(" ");
            }
            for(int j = 1;j<=i ; j++){
                if(i== n || j== i )
                System.out.print("*");
                else
                    System.out.print(" ");
            }
          System.out.println();
        }
}

}

//QUESTION 3
package com.company;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Main {
    public static void main(String[] args)  {
        int n = 5;
        for (int i = 1; i<=n ; i++) {
            for(int j = i; j<=n; j++){
                System.out.print(" ");
            }
            for (int k = 1; k< i; k++) {
                if(i== n || k== 1)
                System.out.print("*");
                else
                    System.out.print(" ");
            }
            for(int j = 1;j<=i ; j++){
                if(i== n || j== i )
                System.out.print("*");
                else
                    System.out.print(" ");
            }
          System.out.println();
        }
}

}


//QUESTION 4
package com.company;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Main {
    public static void main(String[] args)  {
        int numLines = 0;
        int numAlphabets = 0;
        Scanner myFile = null;
        try{
            Scanner file = new Scanner(new File("src/icep.txt"));
            myFile = file;
        } catch (FileNotFoundException e){
            System.out.println("Your file does not exist");
        }
        while(myFile.hasNextLine()){
            //We need the current line
            String curLine = myFile.nextLine();
            int size = curLine.length();
            boolean foundDiv = true;
            boolean foundChar = false;
            for (int i = 0; i < size; i++) {
                if(curLine.charAt(i) == ' '){
                    foundDiv = true;
                    foundChar = false;
                }
                else{
                    foundChar = true;
                    numAlphabets++;

            }
                numLines++;
        }
        //myFile.close();
            System.out.println(("Number of alphabets = "+ numAlphabets));


    }
}

}

CODE RANDOM CODE(TO COUNT THE WORDS IN A TEXT)
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
int numLines = 0;
       int numWords = 0;
       int numChars = 0;
       Scanner myFile = null;
       try{
           Scanner file = new Scanner(new File("src/icep.txt"));
           myFile = file;
       } catch (FileNotFoundException e){
           System.out.println("Your file does not exist");
       }
       while(myFile.hasNextLine()){
           //We need the current line
           String curLine = myFile.nextLine();
           int size = curLine.length();
           boolean foundDiv = true;
           boolean foundChar = false;
           for (int i = 0; i < size; i++) {
               if(curLine.charAt(i) == ' '){
                   foundDiv = true;
                   foundChar = false;
               }
               else{
                   foundChar = true;
                   numChars++;
               }
               if(foundChar && foundDiv){
                   numWords++;
                   foundDiv = false;
               }

           }
           numLines++;
       }
       myFile.close();
       System.out.println(("Number of words = "+ numWords));
       System.out.println(("Number of lines = "+ numLines));
       System.out.println(("Number of chars = "+ numChars));

