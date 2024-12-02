type MinStack struct {
   stack []int
   minstack []int
}


func Constructor() MinStack {
    return MinStack {
        stack: []int{},
        minstack: []int{},
    }
}


func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)
    minval := val
    if len(this.minstack)>0 {
        if this.minstack[len(this.minstack)-1] < minval {
            minval = this.minstack[len(this.minstack)-1]
        }
        this.minstack = append(this.minstack, minval)
    } else {
        this.minstack = append(this.minstack, minval)
    }
}


func (this *MinStack) Pop()  {
    this.stack = this.stack[:len(this.stack)-1]
    this.minstack = this.minstack[:len(this.minstack)-1]
}


func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}


func (this *MinStack) GetMin() int {
    return this.minstack[len(this.minstack)-1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
