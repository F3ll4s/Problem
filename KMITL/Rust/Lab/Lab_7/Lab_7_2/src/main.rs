struct BoxedStack{
    data:Box<Vec<i32>>
}

impl BoxedStack{
    fn new()-> Self{
        BoxedStack{
            data:Box::new(Vec::new())
        }
    }
    fn push(&mut self, value:i32){
        (*self.data).push(value);
        println!("Pushing {} onto the stack", value)
    }
    fn pop(&mut self) -> Option<i32>{
        (*self.data).pop()
    }
    fn peek(&self) -> Option<&i32>{
        if self.data.len() == 0{
            return None;
        }else{
            return Some(&self.data[self.data.len()-1])
        }
    }
    fn is_empty(&self) -> bool{
        if self.data.len() == 0{
            return true;
        }else{
            return false;
        }
    }
    fn print_stack(&self){
        let mut new = (*self.data).clone();
        new.reverse();
        println!("Stack Contents: {:?}", new);
    }

}

fn main() {
    let mut m = BoxedStack::new();
    m.push(10);
    m.push(20);
    m.push(30);
    m.print_stack();
    println!("Top of the stack is {}", m.peek().unwrap());
    println!("Popped {} from the stack", m.pop().unwrap());
    m.print_stack();
    println!("Popped {} from the stack", m.pop().unwrap());
    m.print_stack();
    println!("Popped {} from the stack", m.pop().unwrap());
    m.print_stack();
    println!("Is the stack empty {}", m.is_empty());
}
