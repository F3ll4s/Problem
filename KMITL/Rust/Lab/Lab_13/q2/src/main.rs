mod library;
use library::{LibraryItem,books::Book,media::AudioBook};


fn main() {

    let mut book = Book::new("Somebody");
    let mut audiobook = AudioBook::new("Something");
    println!("{}",book.title());
    println!("{}",audiobook.title());
    println!("{}",book.is_available());
    book.check_out();
    println!("{}",audiobook.is_available());
    audiobook.check_in();
    audiobook.check_out();
    println!("{}",audiobook.is_available());
    let library_items: Vec<&dyn LibraryItem> = vec![
        &book,&audiobook
    ];
    for i in library_items{
        println!("{}",i.title());
    }
}
