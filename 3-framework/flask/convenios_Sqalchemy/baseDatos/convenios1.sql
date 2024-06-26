-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-02-2023 a las 16:57:05
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `convenios1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(166) DEFAULT NULL,
  `tipouser` varchar(166) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `tipouser`, `created_date`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$4YcITo05aZriPQJU$3eb3bd756792d7efef512481ae113afee77ab69203a292ed2fbf4db201b9db0a', '1', '2023-02-02 23:28:27'),
(2, 'myela', 'pbkdf2:sha256:260000$XUD4FKJRBJjnNSmW$82e628116bd625ef3dad8a0beb0fc9e285843312057b887e17b704e4f30e57af', '2', '2023-02-02 23:29:14'),
(3, 'prueba', 'pbkdf2:sha256:260000$PgKMi15gMh192zWw$4c915bfca25a97c2776c39154049f1f15e3a218e448366d40788488f450becfb', '2', '2023-02-03 09:58:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `password` varchar(166) DEFAULT NULL,
  `tipousuario` varchar(166) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `password`, `tipousuario`, `created_date`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$zs2R2ATYptKlyePu$af7b248f15efecb5b3aacefe1fe6080c7a57c0e3b393f0528066d48735e46b05', '1', '2023-02-06 10:56:26'),
(2, 'myela', 'pbkdf2:sha256:260000$5C6ap1iGXATA1QnT$2f397bb5c72b2c7df6c82203368cfda2fa7df8f3e6f0ff70fcfdf06e0d8e4043', '2', '2023-02-06 10:56:46');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
