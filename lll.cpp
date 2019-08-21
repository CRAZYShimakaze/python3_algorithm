#include <iostream>
#include <string.h>
#include <cmath>
#include <algorithm>
using namespace std;
struct Node
{
	int value=0;
	Node *next = NULL;
};
int main()
{
	auto num1 = 345346,num2 = 24579;
	Node* head1 = new Node;
	Node* head2 = new Node;
	auto temp1 = head1;
	auto temp2 = head2;
	while (num1)
	{
		Node* temp = new Node;
		temp->value = num1 % 10;
		num1 /= 10;
		head1->next = temp;
		head1 = temp;
	}
	while (num2)
	{
		Node* temp = new Node;
		temp->value = num2 % 10;
		num2 /= 10;
		head2->next = temp;
		head2 = temp;
		
	}
	temp1 = temp1->next;
	temp2 = temp2->next;
	int flag = 0; int sum = 0;
	Node* head3 = new Node;
	auto temp3 = head3;
	while (temp1 != NULL || temp2 != NULL)
	{	
		if (temp2 == NULL){
			head3->next = temp1;
			break;
		}
		else if(temp1 == NULL){
			head3->next = temp2;
			break;
		}
		Node* temp = new Node;
		sum = temp1->value + temp2->value+flag;
		if (sum > 9) {
			flag = 1;
			sum -= 10;
			temp->value = sum;
		}
		else {
			flag = 0;
			temp->value = sum;
		}
		head3->next = temp;
		head3 = temp;
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	temp3 = temp3->next;
	while (temp3 != NULL) {
		printf("%d\n", temp3->value);
		temp3 = temp3->next;
	}
}