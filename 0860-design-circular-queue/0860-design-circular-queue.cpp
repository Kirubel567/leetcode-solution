class MyCircularQueue {
private: 
    int* arr; 
    int frontIdx, rear, size, MAX; 

public:
    MyCircularQueue(int k) {
        MAX = k; 
        arr = new int[MAX]; 
        size = 0; 
        frontIdx = 0; 
        rear = -1;
    
    }
    
    bool enQueue(int value) {
        if(size == MAX) return false; 
        rear = (rear + 1) % MAX; 
        arr[rear] = value; 
        size++; 

        return true; 
    }
    
    bool deQueue() {
        if(size == 0) return false; 
        frontIdx = (frontIdx + 1) % MAX; 
        size--; 
        return true; 
    }
    
    int Front() {
            if(isEmpty()) return -1; 
            return arr[frontIdx];
        

         
        
    }
    
    int Rear() {
        if(isEmpty()) return -1; 
        return arr[rear]; 
        
    }
    
    bool isEmpty() {
        return size == 0; 
        
    }
    
    bool isFull() {
        return size == MAX; 
        
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */