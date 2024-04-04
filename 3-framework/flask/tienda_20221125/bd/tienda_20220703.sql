-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-07-2022 a las 23:46:09
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `id` smallint(4) UNSIGNED NOT NULL,
  `apellidos` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `nombres` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `fechanacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='almacena datos de los autores';

--
-- Volcado de datos para la tabla `autor`
--

INSERT INTO `autor` (`id`, `apellidos`, `nombres`, `fechanacimiento`) VALUES
(1, 'Vallejo Mendoza', 'César Abraham', '1892-03-16'),
(2, 'Vargas Llosa', 'Jorge Mario Pedro', '1936-03-28'),
(3, 'Alegría Bazán', 'Ciro', '1909-11-04'),
(4, 'García Márquez', 'Gabriel José de la Concordia', '1927-03-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE `compra` (
  `uuid` char(36) COLLATE utf8_unicode_ci NOT NULL,
  `libro_isbn` char(12) COLLATE utf8_unicode_ci NOT NULL,
  `usuario_id` smallint(3) UNSIGNED NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='almacena las compras';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `isbn` char(12) COLLATE utf8_unicode_ci NOT NULL,
  `titulo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `autor_id` smallint(4) UNSIGNED NOT NULL,
  `anoedicion` year(4) NOT NULL,
  `precio` decimal(3,0) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='libros';

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`isbn`, `titulo`, `autor_id`, `anoedicion`, `precio`) VALUES
('238874100138', 'Conversación en La Catedral', 2, 1951, '70'),
('383370912281', 'El mundo es ancho y ajeno', 3, 1941, '65'),
('480129403571', 'La ciudad y los perros', 2, 1963, '81'),
('483240184226', 'La serpiente de oro', 3, 1935, '85'),
('589120131047', 'Los perros hambrientos', 3, 1939, '31'),
('591338770183', 'Paco Yunque', 1, 1951, '55'),
('661984010128', 'El general en su laberinto', 4, 1989, '110'),
('683425019133', 'El coronel no tiene quien le escriba', 4, 1961, '42'),
('762841019387', 'Cien años de soledad', 4, 1967, '75'),
('890366138239', 'La fiesta del Chivo', 2, 2000, '30'),
('892014771852', 'Poemas humanos', 1, 1939, '120'),
('930281938211', 'El amor en los tiempos del cólera', 4, 1985, '38'),
('978318472263', 'Los heraldos negros', 1, 1919, '48'),
('981402938251', 'La casa verde', 2, 1966, '105');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipousuario`
--

CREATE TABLE `tipousuario` (
  `id` tinyint(1) UNSIGNED NOT NULL,
  `nombre` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='almacena tipo de usuarios';

--
-- Volcado de datos para la tabla `tipousuario`
--

INSERT INTO `tipousuario` (`id`, `nombre`) VALUES
(1, 'Administrador'),
(2, 'Cliente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `usuario` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` char(102) COLLATE utf8_unicode_ci NOT NULL,
  `tipousuario_id` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='almacena usuarios';

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `password`, `tipousuario_id`) VALUES
(1, 'myela', 'pbkdf2:sha256:260000$1XLOIX0GEBfbOGkJ$8a5528fb246f865b3f5b2cfecb65cb33956346f243fe16895c653d61ab6a33e7', 2),
(2, 'gremaurga', 'pbkdf2:sha256:260000$v4COaIHCa30C6vVC$e751086856398e1d87103eb24cecb9c9abf920f748cd53a4e0e2977a0fbed289', 2),
(3, 'admin', 'pbkdf2:sha256:260000$1XLOIX0GEBfbOGkJ$8a5528fb246f865b3f5b2cfecb65cb33956346f243fe16895c653d61ab6a33e7', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`uuid`),
  ADD KEY `FK_compra_libro` (`libro_isbn`),
  ADD KEY `FK_compra_usuario` (`usuario_id`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `FK_libro_autor` (`autor_id`);

--
-- Indices de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_usuario_tipousuario` (`tipousuario_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `id` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `id` tinyint(1) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `FK_compra_libro` FOREIGN KEY (`libro_isbn`) REFERENCES `libro` (`isbn`),
  ADD CONSTRAINT `FK_compra_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `FK_libro_autor` FOREIGN KEY (`autor_id`) REFERENCES `autor` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `FK_usuario_tipousuario` FOREIGN KEY (`tipousuario_id`) REFERENCES `tipousuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
