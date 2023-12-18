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

let particles = create(200, "yellow");

let update = () => {
    m.clearRect(0, 0, 500, 500);
    draw(0, 0, "black", 500);

    for (let i = 0; i < particles.length; i++) {
        let p = particles[i];
        draw(p.x, p.y, p.color, 5);
    }

    requestAnimationFrame(update);
};

update();
