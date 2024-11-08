// Example of multiple structs implementing the same trait in Rust

// Define a trait for printable objects
trait Printable {
    fn print(&self);
    fn print_email(&self);
}

// Define the Person struct
pub struct Person {
    name: String,
    age: u32,
    email: Option<String>,
}

// Define the Company struct
pub struct Company {
    name: String,
    year: u32,
    email: Option<String>,
    address: String,
}

// Implement methods for Person
impl Person {
    pub fn new(name: String, age: u32) -> Self {
        Person {
            name,
            age,
            email: None,
        }
    }

    pub fn set_email(&mut self, email: String) {
        self.email = Some(email);
    }
}

// Implement methods for Company
impl Company {
    pub fn new(name: String, year: u32, address: String) -> Self {
        Company {
            name,
            year,
            email: None,
            address,
        }
    }

    pub fn set_email(&mut self, email: String) {
        self.email = Some(email);
    }
}

// Implement the Printable trait for Person
impl Printable for Person {
    fn print(&self) {
        println!("Name: {}", self.name);
        println!("Age: {}", self.age);
        match &self.email {
            Some(email) => println!("Email: {}", email),
            None => println!("Email: Not provided"),
        }
    }
    
    fn print_email(&self) {
        println!("Name: {}", self.name);
        match &self.email {
            Some(email) => println!("Email: {}", email),
            None => println!("Email: Not provided"),
        }
    }
}

// Implement the Printable trait for Company
impl Printable for Company {
    fn print(&self) {
        println!("Company: {}", self.name);
        println!("Founded: {}", self.year);
        match &self.email {
            Some(email) => println!("Email: {}", email),
            None => println!("Email: Not provided"),
        }
        println!("Address: {}", self.address);
    }
    
    fn print_email(&self) {
        println!("Company: {}", self.name);
        match &self.email {
            Some(email) => println!("Email: {}", email),
            None => println!("Email: Not provided"),
        }
        println!("Address: {}", self.address);
    }
}

// Main function to demonstrate usage
fn main() {
    // Create a new Person
    let mut john = Person::new("John Doe".to_string(), 30);
    john.set_email("john.doe@example.com".to_string());

    // Create a new Company
    let mut acme = Company::new("Acme Corp".to_string(), 1985, "123 Main St, Anytown, USA".to_string());
    acme.set_email("info@acmecorp.com".to_string());

    // Demonstrate polymorphism
    let printables: Vec<&dyn Printable> = vec![&john, &acme];

    println!("Printing all printable objects:");
    for printable in &printables {
        printable.print();
        println!(); // Add a blank line between prints
    }

    println!("Printing emails of all printable objects:");
    for printable in &printables {
        printable.print_email();
        println!(); // Add a blank line between prints
    }
}