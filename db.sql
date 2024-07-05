create database if not exists cacRecetas;

use cacRecetas;

create table users (
`id` INT UNSIGNED PRIMARY KEY auto_increment,
`nombre` varchar(255) NOT NULL,
`contraseña` varchar(255) NOT NULL
);

insert into users VALUES
(default,"juan","1234"),(default,"andrés","1234"),(default,"maría","1234");


create table recetas (
`id` INT UNSIGNED PRIMARY KEY auto_increment,
`titulo` varchar(255) NOT NULL,
`descripion` varchar(500) NOT NULL,
`ingredientes` varchar(400) NOT NULL,
`preparacion` varchar(900) NOT NULL,
`imagen` varchar(300) NOT NULL,
`usuarioId` INT UNSIGNED,
FOREIGN KEY (`usuarioId`) REFERENCES users(`id`)
);


INSERT INTO recetas (titulo, descripion, ingredientes, preparacion, imagen, usuarioId)
VALUES
  ('Torta de Chocolate', 'Deliciosa torta de chocolate', '200 g de chocolate negro, 150 g de mantequilla, 150 g de azúcar, 4 huevos, 100 g de harina', '1. Derrite el chocolate y la mantequilla juntos. 2. Bate los huevos con el azúcar hasta que estén espumosos. 3. Agrega la mezcla de chocolate derretido a los huevos.', 'https://resizer.glanacion.com/resizer/v2/torta-de-chocolate-5G4LZ5WTM5H4RHWT257DEGRZQU.jpg?auth=a69092357dfe5b42c4142471e922c292fe15dbf2541c260bf07656c09ea998b7&width=768&height=512&quality=70&smart=true', '1'),
  ('Ensalada César', 'Clásica ensalada con pollo y aderezo César', 'Lechuga romana, pollo a la parrilla, croutones, queso parmesano, aderezo César', '1. Lava y corta la lechuga. 2. Agrega el pollo a la ensalada. 3. Espolvorea con croutones y queso parmesano. 4. Rocía con aderezo César.', 'https://cuk-it.com/wp-content/uploads/2022/02/ensalada-caesar-pasta.webp', '2'),
  ('Sushi de Salmón', 'Rollos de sushi con salmón fresco', 'Arroz para sushi, alga nori, salmón fresco, aguacate, pepino', '1. Extiende el arroz sobre el alga nori. 2. Agrega tiras de salmón, aguacate y pepino. 3. Enrolla y corta en rodajas.', 'https://imag.bonviveur.com/sushi-casero.jpg', '3'),
  ('Pizza Margarita', 'Pizza clásica con tomate, mozzarella y albahaca', 'Masa de pizza, salsa de tomate, mozzarella, albahaca fresca', '1. Extiende la masa de pizza. 2. Agrega salsa de tomate y mozzarella. 3. Hornea hasta que esté dorada. 4. Decora con albahaca fresca.', 'https://www.foodandwine.com/thmb/Wd4lBRZz3X_8qBr69UOu2m7I2iw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-cheese-pizza-FT-RECIPE0422-31a2c938fc2546c9a07b7011658cfd05.jpg', '1'),
  ('Pastel de Zanahoria', 'Postre esponjoso con zanahoria y nueces', 'Zanahorias ralladas, nueces picadas, harina, azúcar, huevos', '1. Mezcla las zanahorias ralladas con las nueces. 2. Agrega la mezcla de harina, azúcar y huevos. 3. Hornea hasta que esté cocido.', 'https://www.elmueble.com/medio/2018/12/18/detalle-de-pastel-de-zanahoria_00000000_230201131818_600x600.jpg', '2');

