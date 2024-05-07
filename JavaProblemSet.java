

import java.util.*;

public class JavaProblemSet {
    public static void main(String[] args){
// greeting
		
		Scanner s = new Scanner(System.in);

		System.out.println("Welcome, what is your name?");
		

		String name = s.nextLine();


	//Concatenate strings by adding them together
		String response = ""; 
		response = "Hello" + name + "!";
		System.out.println(response);

        // 2.isTriangle 
        System.out.println("Type the length of side a:");
        int sideA = s.nextInt();

        System.out.println("Type the length of side b:");
        int sideB = s.nextInt();

        System.out.println("Type the length of side c:");
        int sideC = s.nextInt();

        if (Triangle(sideA, sideB, sideC)) {  
            System.out.println("The given side lengths can form a triangle.");
        } else {
            System.out.println("The given side lengths cannot form a triangle.");
        }

        //4.duplicates

   int[] duplicate = {4, 4, 10, 12, 15, 5, 5, 10};

       
        System.out.print("{");
        for (int i = 0; i < duplicate.length - 1; i++) {
            if (duplicate[i] == duplicate[i + 1]) {
                if (i > 0) {
                    System.out.print(",");
                }
                System.out.print(duplicate[i]);
            }
        }
        System.out.println("}");
   

//6.guessNumber

     
         if (guessNumber(14)) {  
            System.out.println("Congratulations! You guessed the number correctly.");
        } else {
            System.out.println("Sorry! You couldn't guess the number correctly.");
        }


        }
    


// method call for isTriangle
    public static boolean Triangle(int a, int b, int c) {
      
        return (a + b > c) && (a + c > b) && (b + c > a);
    }


   //method call for guessNumber

     public static boolean guessNumber(int x) {


        Scanner scanner = new Scanner(System.in);
        int minRange = 1;
        int maxRange = 20;

       
        for (int i = 0; i < 2; i++) {
            System.out.println("Guess a number between " + minRange + " and " + maxRange + ":");
            int guess = scanner.nextInt();

            if (guess < x) {
                System.out.println("The number is greater than " + guess + ". Try again.");
                minRange = guess + 1;
            } else if (guess > x) {
                System.out.println("The number is less than " + guess + ". Try again.");
                maxRange = guess - 1;
            } else {
                return true; 
            }
        }

        return false; // Couldn't guess correctly within 2 attempts

        

    }



}


