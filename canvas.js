let m = document.getElementById("life").getContext("2d");

if (!m) {
    console.error("Canvas context not obtained");
}

let draw = (x, y, c, s) => {
    m.fillStyle = c;
    m.fillRect(x, y, s, s);
};

let particle = (x, y, c) => {
    return { "x": x, "y": y, "vx": 0, "vy": 0, "color": c };
};

let random = () => {
    return Math.random() * 400 + 50;
};

let create = (number, color) => {
    let group = [];
    for (let i = 0; i < number; i++) {
        group.push(particle(random(), random(), color));
    }
    return group;
};
let particlesList = ["blue", "yellow", "red"]
let allParticles = [] // empty list to push particles 
//let particles = create(200, "red");
for(let i = 0; i<particlesList.length; i++){
    let particles = create(200, particlesList[i])
    allParticles.push(particles)
}

let update = () => {
    m.clearRect(0, 0, 500, 500);
    draw(0, 0, "black", 500);

    for(let group of allParticles){
        for (let p of group){
            draw(p.x,p.y, p.color, 5);
        }
    }

    requestAnimationFrame(update);
};

update();
