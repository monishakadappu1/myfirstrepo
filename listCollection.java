package javaapplication20;
import java.util.*;

class Node
{

	int data;
	Node next;

	public Node(int data){
		this.data=data;
		this.next=null;

	}
}

public class listCollection
{
	Node addNode(int data,Node head){ // java does not support default args
		if(head==null){
                    head=new Node(data);
                    head.next=null;
                    return head;
                }
                Node N1=new Node(data);
		head.next=N1;
		N1.next=null;
		if(N1!=null){return N1;}
		else{return null;}
	}

	Node delNode(int value,Node present)
	{
		int temp=0;
		Node first=present;
		if (present==null)
			{System.out.println("The list is empty");
			temp=0;
		}
		//while(present.next!=0)
		else if(present.next==null)
		{
			System.out.println("Single linked list");
			temp=first.data;
			first=present=null;
			//return temp;
		}
		else{
			Node prev=null;
			while(present.next!=null){
				if(present.data==value){
					break;
				}
				else{
					prev=present;
					present=present.next;
				}
				
			}
			System.out.println("Proper linked list");
			temp=present.data;
			prev.next=present.next;
			//return temp;
			//return head;

		}
		return first;

	}
	void display(Node head){
		if (head==null){
			System.out.println("Empty list");
		}
		else if(head.next==null){
			System.out.println("Single element list");
			System.out.println(head.data);
		}
		else{
			Node present=head;
			while(present.next!=null){
				System.out.println(present.data);
				present=present.next;
			}
			System.out.println(present.data);
			System.out.println("End of the list");
		}
	}

	public static void main(String[] args){
		listCollection list1=new listCollection();
		int val;
                Node head=null;
		list1.display(head);
		head=list1.addNode(1,head);
		list1.display(head);
		head=list1.delNode(1,head);
		list1.display(head);
		Node curr=null;
		Node prev=null;
		for(int i=1;i<10;i++)
		{
			if (prev==null){
				head=list1.addNode(i,head);
				prev=head;
			}
			else{
				curr=list1.addNode(i,prev);
				prev=curr;
			}
			
		}
		list1.display(head);
		curr=head;
		for(int j=1;j<5;j++){
			curr=list1.delNode(j,curr);
			curr=curr.next;
		}
		list1.display(head);
	}


}