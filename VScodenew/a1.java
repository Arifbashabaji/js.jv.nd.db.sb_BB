import java.util.*;

class main1{
    public static void main(String [] args)
    {
        HashMap<Character,String> a6=new HashMap<>();
        
        StringBuilder s1=new StringBuilder("BRO");
        
        s1.append(1);
        s1.insert(2,'%');

        System.out.println(s1.toString());
        s1.delete(2,3);
        System.out.println(s1.charAt(2));
        System.out.println(s1.indexOf("1"));
        // boolean a=Character.isLowerCase(s1.charAt(0));
        // System.out.println(a);
        System.out.println(s1.toString());
        String s2=s1.toString();
        String s4=s2.substring(1);
        System.out.println(s2.length());
        System.out.println(s4.length());
        System.out.println(s4);
        char[] b=s2.toCharArray();
        for(char a3:b){
            a6.put(a3,"@");
        }
        for(char a4:b){
        System.out.println(a6.get(a4));
        a6.remove(a4);
        System.out.println(a6.containsKey(a4));
        }
        int[] arr=new int[10];
        Scanner s=new Scanner(System.in);
        for(int i=0;i<arr.length && s.hasNextInt();i++){
            arr[i]=s.nextInt();}
        s.close();
            for(int a11:arr)
            System.out.println(a11);
            Arrays.sort(arr);
                  for(int a11:arr)
            System.out.println(a11);
            int[] arr1=Arrays.copyOfRange(arr,1,8);
            System.out.println("_________________________________________");
            for(int i:arr1){System.out.println(i);}
    }}
