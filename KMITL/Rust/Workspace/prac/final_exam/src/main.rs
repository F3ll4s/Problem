fn matrix_mul(a:[[i32;3];2],b:[[i32;3];3]){
    let mut final_rr:[[i32;3];2] = a.clone();
}








fn main() {
    let a: [[i32;3];2] =[ 
        [1,2,3],
        [4,5,6],
    ];
    
    let b :[[i32;3];3] = [
        [7,8,9],
        [10,11,12],
        [13,14,15],
    ];


    println!("Matrix 1: {:?}" ,a);
    println!("Matrix 2: {:?}", b);

    let mut answer = matrix_mul(a,b);
    println!("{:?}", answer);
}
