struct Fibonacci{
    current:u32,
    value:u32
}

impl Fibonacci{
    fn new() -> Self{
        Fibonacci{current: 0,value : 1}
    }
}

impl Iterator for Fibonacci{
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item>{
        let temp = self.current;
        self.current = self.value;
        self.value += temp;
        Some(temp)
    }
}


fn main(){
    let fibonac = Fibonacci::new();
    for (i, num) in fibonac.enumerate().take(10) {
        println!("Fibonacci {} = {}", i + 1, num);
    }
    
}








// fn fibo (x:i32) -> i32{
//     if x == 0 && x == 1{
//         return 1
//     }
//     return fibo(x-1) + fibo(x-2)
// }

// fn main() {
//     println!("{}",fibo(5));
// }
