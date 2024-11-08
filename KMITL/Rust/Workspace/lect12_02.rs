struct Person {
    first_name: String,
    last_name: String,
    age: u32,
}

impl Person {
    // Method that takes self by value (consumes the instance)
    fn introduce(self) {
        println!("Hi, I am {} {} and I am {} years old.", self.first_name, self.last_name, self.age);
        // After this method, `self` is consumed and can't be used anymore
    }
    
    // Method that takes &self (borrows immutably)
    fn full_name(&self) -> String {
        format!("{} {}", self.first_name, self.last_name)
    }
    
    // Method that takes &mut self (borrows mutably)
    fn birthday(&mut self) {
        self.age += 1;
        println!("Happy birthday, {}! You are now {} years old.", self.full_name(), self.age);
    }
}

fn main() {
    // Creating an instance of Person
    let mut person = Person {
        first_name: "John".to_string(),
        last_name: "Doe".to_string(),
        age: 30,
    };
    
    // Calling the &self method (immutable borrow)
    println!("Full Name: {}", person.full_name());
    
    // Calling the &mut self method (mutable borrow)
    person.birthday(); // This changes the age of the person
    
    // Calling the self method (consumes the instance)
    person.introduce();
    
    println!("{}", person.full_name());
}
