// import java.lang.*;
import java.util.*;
public class nov9gencnext {
    public static void main(String[] args)
    {
        String s1="NEW String";
        StringBuilder sb=new StringBuilder(s1).reverse();
        sb.append("DHTDHD");
        sb.insert(1,"@@@@@@@@@@@@@@@");
        sb.delete(0,1);
        HashMap<Integer,String> h1=new HashMap<>();
        // HashMap<Character,String> a6=new HashMap<>();
        h1.put(1,"One");
        h1.put(2,"Two");
        h1.put(3,"3");
        h1.put(2,"2");
        int[] keys={3,2,1,2};
        
        for(int i:keys){
            if(h1.containsKey(i)==true)
            {
                System.out.print("im in");
                System.out.println(h1.get(i));
                // String s2=Integer.toString(4);
            }
        }
        h1.remove(2,"Two");
        System.out.println(h1.entrySet()+" ||||| "+h1.size());
        h1.remove(2,"2");
        System.out.println(h1.entrySet()+" ||||| "+h1.size());
    
        int a=10;
        float f=21.1f;
        System.out.println(s1+"  "+sb.toString()+"  "+a+"  "+f);
        int[] arr1={1,2,3,4,9,6,7,5};
        // for(int j:arr1)
        // {
        //     // System.out.print(j);
        // }
        Arrays.sort(arr1);
        // for(int j:arr1)
        // {
        //     // System.out.print(j);
        // }
        int[] arr2=Arrays.copyOfRange(arr1,0,3);
for(int j:arr2)
        {
            System.out.print(j+" ");
        }
        arr2[1]=122;
        for(int j:arr2)
        {
            System.out.print(j+" ");
        }
        char[] c1=s1.toCharArray();
        String k=new String(c1);
        System.out.println(k);
        // System.out.println(Arrays.binarySearch(arr1,2));
    }
}
