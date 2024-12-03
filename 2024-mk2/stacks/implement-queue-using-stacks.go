type MyQueue struct {
    stack []int
    stack2 []int
}


func Constructor() MyQueue {
    return MyQueue {
        stack: []int{},
        stack2: []int{},
    }
}


func (this *MyQueue) Push(x int)  {
    this.stack = append(this.stack, x)
}


func (this *MyQueue) Pop() int {
    // need to get the element at the bottom of the stack

    for i := len(this.stack)-1; i>=0; i-- {
        this.stack2 = append(this.stack2, this.stack[i])
        this.stack = this.stack[:i]
    }
    tmp := this.stack2[len(this.stack2)-1] 

    for i := len(this.stack2)-2; i>=0; i-- {
        this.stack = append(this.stack, this.stack2[i])
        this.stack2 = this.stack2[:i]
    }
    
    return tmp
}


func (this *MyQueue) Peek() int {
    // need to get the element at the bottom of the stack

    for i := len(this.stack)-1; i>=0; i-- {
        this.stack2 = append(this.stack2, this.stack[i])
        this.stack = this.stack[:i]
    }
    tmp := this.stack2[len(this.stack2)-1] 
    
    for i := len(this.stack2)-1; i>=0; i-- {
        this.stack = append(this.stack, this.stack2[i])
        this.stack2 = this.stack2[:i]
    }
    
    return tmp
    
}


func (this *MyQueue) Empty() bool {
    if len(this.stack) > 0 {
        return false
    }
    return true
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 *
