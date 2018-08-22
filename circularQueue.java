/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

import java.util.*;



// Class linkedList<T>{



// 	linkedList(){

// 		T data= 0;

// 		linkedList nextNode=Null;

// 	}



// 	<T> void addNode(T val,linkedList obj){

// 		data=val;

// 		nextNode=obj;

// 	}



// 	<T> T removeNode()





// }



public class circularQueue{


    int front;
    int rear;
    int arr[];

    int max1;
	circularQueue(int max1){

		this.max1=max1;

		front=-1;

		rear=-1;

		arr=new int[max1];

	}



	void enQueu(int data){
                System.out.println("rear index at "+rear);
		if ((rear+1==max1 && front==0) || (rear==front-1)){

			System.out.println("queue full");

		}
                else if(rear+1==max1){
                    rear=0;
                    arr[rear]=data;
                }

		else{

			if((rear==-1)&&(front==-1))

			{
                                System.out.println("making rear 0");
				rear=0;

				front=0;

				arr[rear]=data;

			}

			else{

				rear++;

				arr[rear]=data;

			}

		}

		System.out.println("afetr enQue "+ arr[rear]+"with rear index at "+rear);

	}



	int deQueue(){
                int gotcha=0;
		if(rear==-1 && front==-1){

			System.out.println("queue is empty to delete");



		}

		else if(rear==front){

			System.out.println("one element queue");

			 gotcha=arr[front];

			rear=front=-1;

			return gotcha;

		}

		else{
                        System.out.println("deletiong one element ");
			gotcha=arr[front];
                        arr[front]=0;
			if(front+1==max1){front=0;}

                        else{front++;}

			//return gotcha;

		}

                return gotcha;

	}



	void display()

	{

		for(int i=0;i<arr.length;i++)

		{

			System.out.println(arr[i]);

		}

	}



	public static void main(String []args){



		circularQueue Q1=new circularQueue(7);

		Q1.enQueu(1);

		Q1.enQueu(2);

		Q1.enQueu(3);

		Q1.enQueu(4);

		Q1.enQueu(5);
                Q1.enQueu(6);
                Q1.enQueu(7);

		Q1.display();

		Q1.deQueue();
                Q1.deQueue();
                Q1.deQueue();

		Q1.display();
                Q1.enQueu(3);
                Q1.enQueu(4);
                Q1.display();


	}





}