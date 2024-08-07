use rand::Rng;
use std::io;

#[derive(Clone,Debug)]
struct Player{
    hp:i32,
    stamina:i32,
    power:i32,
    gold:i32,
    maxhp:i32,
}

#[derive(Clone,Debug)]
struct Enemy{
    name:String,
    hp:i32,
    stamina:i32,
    power:i32,
    id:i32,
}

enum Move{
    North,
    South,
    East,
    West
}

enum Encounter{
    Nothing,
    Bush,
    Meat,
    Water,
    Herb,
    IronOre,
    Enemy
}


impl Move{
    fn get_direction(&self){
        match self{
            Move::North => println!("You moved to the North"),
            Move::South => println!("You moved to the South"),
            Move::East => println!("You moved to the East"),
            Move::West => println!("You moved to the West"),
        }
    }
}
impl Player{
    fn new() -> Player{
        Player{
        hp: 100,
        stamina : 50,
        power : 10,
        gold : 0,
        maxhp : 100,
        }
    }
    fn fight_flee(&mut self,mut x:Enemy){
        loop {
            println!("{:?}",self);
            println!("{:?}",x);
            if self.hp <= 0{
                println!("You died ");
                self.hp = 0;
                break;
            }else{
                if x.hp <= 0{
                    match x.id{
                        0 => {
                            println!("You killed Rat");
                            self.gold += 10;
                            break;
                        }
                        1 => {
                            println!("You killed Wolf");
                            self.gold += 20;
                            break;
                        }
                        2 => {
                            println!("You killed Boar");
                            self.gold += 30;
                            break;
                        }
                        3 => {
                            println!("You killed Tiger");
                            self.gold += 40;
                            break;
                        }
                        4 =>{
                            println!("You killed Dragon");
                            self.gold += 60;
                            break;
                        },
                        _ => println!("Nothing"),
                    }
                }
            }
            let mut z = String::new();
            println!("(1) Fight (2) Flee: ");
            io::stdin().read_line(&mut z).expect("Failed to read");
            let mut y = match z.trim().parse(){
                Ok(1) => 1,
                Ok(2) => 2,
                Ok(_) => {
                    println!("Wrong Input");
                    continue;
                }
                Err(_) => {
                    println!("Wrong Input");
                    continue;
                }
            };
            match y {
                1 => {
                    self.stamina -= 1;
                    let mut playerrng = rand::thread_rng().gen_range(1..=100);
                    let mut enemyrng = rand::thread_rng().gen_range(1..=100);
                    if playerrng <= (100 - x.stamina/2){
                        println!("Player Hit");
                        x.hp -= self.power;
                        if x.hp <= 0 {
                            println!("Enemy killed");
                            break;
                        }
                    } else {
                        println!("Player Missed");
                    }
                    if enemyrng <= (100 - self.stamina/2){
                        println!("Enemy Hit");
                        self.hp -= x.power;
                    }else{
                        println!("Enemy Missed");
                    } 
                }
                2 => {
                    self.stamina -= 2;
                    let mut chance = rand::thread_rng().gen_range(1..=100);
                }

                _ => {
                    continue;
                }
            }
        
        }
    }
    fn encounter(&self)-> Encounter{
        let mut en = rand::thread_rng().gen_range(1..=100);
        match en{
            1..=16 => Encounter::Nothing,
            17..=26 => Encounter::Bush,
            27..=39 => Encounter::Meat,
            40..=54 => Encounter::Water,
            55..=69 => Encounter::Herb,
            70..=74 => Encounter::IronOre,
            _ => Encounter::Enemy,
        }
    }
    fn get_encounter(&mut self, x: Encounter, y: Vec<Enemy>) {
        match x {
        Encounter::Nothing => {
            self.stamina -= 1 ;
            println!("You found Nothing");
        }
        Encounter::Bush => {
            self.stamina -= 2 ;
            println!("You walked in to a bush. Your stamina is now {}",self.stamina);
        },
        Encounter::Meat =>{
            self.hp += 4 ;
            self.stamina -= 1 ;
            println!("You found Meat. Your hp is now {}",self.hp);
        }
        Encounter::Water =>{
            self.stamina += 2;
            self.stamina -= 1 ;
            println!("You found Water. Your stamina is now {}",self.stamina);
        }
        Encounter::Herb =>{
            self.power += 1 ;
            self.stamina -= 1 ;
            println!("You found Herb. Your power is now {}",self.power);
        }
        Encounter::IronOre =>{
            self.power += 10 ;
            self.stamina -= 1 ;
            println!("You found IronOre. Your power is now {}",self.power);
        }
        Encounter::Enemy =>{
            let mut enemy_type = match rand::thread_rng().gen_range(1..=100){
                1..=44 => self.fight_flee(y[0].clone()),
                45..=69 => self.fight_flee(y[1].clone()),
                70..=84 => self.fight_flee(y[2].clone()),
                85..=94 => self.fight_flee(y[3].clone()),
                _ => self.fight_flee(y[4].clone())
                };
            }
        }
    }   
}



fn main(){
    let mut player = Player::new();
    let enemy:Vec<Enemy> = vec![
        Enemy{
            name: "Rat".to_string(),
            hp: 10,
            stamina:20,
            power: 2,
            id:0,
        },
        Enemy{
            name: "Wolf".to_string(),
            hp: 20,
            stamina:20,
            power: 10,
            id:1,
        },
        Enemy{
            name: "Boar".to_string(),
            hp: 30,
            stamina:40,
            power: 20,
            id:2,
        },
        Enemy{
            name: "Tiger".to_string(),
            hp: 40,
            stamina:50,
            power: 30,
            id:3,
        },
        Enemy{
            name: "Dragon".to_string(),
            hp: 60,
            stamina:60,
            power: 40,
            id:4,
        }
    ];
    let mut input = String::new();
    loop{
        println!("(1) North (2) South (3) East (4) West (9) Exit game");
        io::stdin().read_line(&mut input).expect("Failed to read");
        let xyz = match input.trim().parse(){
            Ok(1) => Move::North,
            Ok(2) => Move::South,
            Ok(3) => Move::East,
            Ok(4) => Move::West,
            Ok(9) => {
                println!("Thank you for Playing");
                break;
            }
            Ok(_) =>{
                println!("Wrong Input. Type it Again");
                continue;
            }
            Err(_) =>{
                println!("Wrong Input. Type it Again");
                continue;
            }
        };
        input.clear();
        xyz.get_direction();
        let p = player.encounter();
        player.get_encounter(p, enemy.clone());
    }
}