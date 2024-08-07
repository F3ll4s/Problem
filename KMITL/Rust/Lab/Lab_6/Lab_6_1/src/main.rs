fn swap_element<T>(a:Vec<T>,b:Vec<T>)->(Vec<T>,Vec<T>){
    (b,a)
}

fn main(){
    let vec1 = vec![1,2,3];
    let vec2 = vec![4,5,6];
    let result = swap_element(vec1,vec2);
    println!("{:?} ", result);
}