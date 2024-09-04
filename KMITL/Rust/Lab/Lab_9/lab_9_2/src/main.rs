fn main() {
    let mut wtf: Vec<i32> = Vec::new();
    println!("The initial length is {} The capacity is {}", wtf.len(),wtf.capacity());
    for i in 0..5{
        wtf.push(i);
    }
    println!("The initial length is {} The capacity is {}", wtf.len(),wtf.capacity());
    let mut wtf2 = Vec::with_capacity(10);
    for i in 0..15{
        wtf2.push(i);
    }
    println!("The initial length is {} The capacity is {}", wtf2.len(),wtf2.capacity());
}
