fn matrix_mul(a: [[i32;3];2],b: [[i32;3];3])-> [[i32;3];2] {
    let mut final_r:[[i32;3];2] = a.clone();
    for i in 0..a.len(){
        let mut final_arr:[i32;3] = [0,0,0];
        for j in 0..b[0].len(){
            let mut total: i32 = 0;
            for k in 0..a[0].len(){
                let result:i32 = a[i][k] * b[k][j];
                total += result;
            }
            final_arr[j]= total;
        }
        final_r[i] = final_arr;
    }
    return final_r;
}

fn main(){
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