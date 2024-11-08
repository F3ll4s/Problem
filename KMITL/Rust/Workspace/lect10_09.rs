// Define a struct for our custom factorial iterator
struct Factorial {
    current: u64,
    value: u64,
}

// Implement the Iterator trait for our Factorial struct
impl Iterator for Factorial {
    // Specify the type of item this iterator will produce
    type Item = u64;

    // Implement the next() method
    fn next(&mut self) -> Option<Self::Item> {
        // Calculate the current factorial value
        self.value *= self.current;
        
        // Increment the current number
        self.current += 1;

        // Return the factorial value
        Some(self.value)
    }
}

// Implement a constructor for our Factorial iterator
impl Factorial {
    fn new() -> Factorial {
        Factorial { current: 1, value: 1 }
    }
}

fn main() {
    // Create a new Factorial iterator
    let fact = Factorial::new();

    // Use the iterator to print the first 10 factorial numbers
    for (i, num) in fact.enumerate().take(5) {
        println!("{}! = {}", i + 1, num);
    }

   let fact_vec : Vec<usize> = fact.enumerate().take(5).collect();
}