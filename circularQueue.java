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

Class circularQueue{

	circularQueue(int max){
		this.max=max;
		int front=-1;
		int rear=-1;
		int arr=new int(max);
	}

	void enQueu(int data){
		if ((rear+1==max && front=0) || (rear=front-1)){
			System.out.println("queue full");
		}
		else{
			if((rear==-1)&&(front==-1))
			{
				rear+=1;
				front+=1;
				arr[rear]=data;
			}
			else{
				rear++;
				arr[rear]=data;
			}
		}
		System.out.println("afetr enQue "+ arr[rear]);
	}

	int deQueue(){
		if(rear==-1 && front==-1){
			System.out.println("queue is empty to delete");

		}
		else if(rear==front){
			System.out.println("one element queue");
			int gotcha=arr[front];
			rear=front=-1;
			return gotcha;
		}
		else{
			int gotcha=arr[front];
			if(front+1===max){front=0;}
			else(front++;)
			return gotcha
		}

	}

	void display()
	{
		for(int i=0;i<arr.length();i++)
		{
			System.out.println(arr[i]);
		}
	}

	Public static void main(String []args){

		circularQueue Q1=new circularQueue(7);
		Q1.enQueu(1);
		Q1.enQueu(2);
		Q1.enQueu(3);
		Q1.enQueu(4);
		Q1.enQueu(5);
		Q1.display();
		Q1.deQueue();
		Q1.display();

	}


}