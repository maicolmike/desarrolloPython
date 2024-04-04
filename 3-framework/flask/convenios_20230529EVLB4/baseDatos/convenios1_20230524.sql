-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 192.168.17.82    Database: convenios1
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tipousuario`
--

DROP TABLE IF EXISTS `tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipousuario` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipousuario`
--

LOCK TABLES `tipousuario` WRITE;
/*!40000 ALTER TABLE `tipousuario` DISABLE KEYS */;
INSERT INTO `tipousuario` VALUES (1,'Administrador'),(2,'Cliente');
/*!40000 ALTER TABLE `tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(166) DEFAULT NULL,
  `tipouser` varchar(166) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','pbkdf2:sha256:260000$4YcITo05aZriPQJU$3eb3bd756792d7efef512481ae113afee77ab69203a292ed2fbf4db201b9db0a','1','2023-02-02 23:28:27'),(2,'myela','pbkdf2:sha256:260000$XUD4FKJRBJjnNSmW$82e628116bd625ef3dad8a0beb0fc9e285843312057b887e17b704e4f30e57af','2','2023-02-02 23:29:14'),(3,'prueba','pbkdf2:sha256:260000$PgKMi15gMh192zWw$4c915bfca25a97c2776c39154049f1f15e3a218e448366d40788488f450becfb','2','2023-02-03 09:58:55');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) DEFAULT NULL,
  `email` varchar(65) DEFAULT NULL,
  `password` varchar(166) DEFAULT NULL,
  `tipousuario` tinyint unsigned NOT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `FK_USUARIO_TIPOUSUARIO` (`tipousuario`),
  CONSTRAINT `FK_USUARIO_TIPOUSUARIO` FOREIGN KEY (`tipousuario`) REFERENCES `tipousuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Admin11','soportesistemas@cootep.com.co','pbkdf2:sha256:260000$105HDQKkAJ6mkECC$3c76f06bd2bf8c5eb36085648421740e8c2f5d2e18baaf8e0b573b48b2964720',1,'2023-02-06 10:56:26'),(2,'myela','maicol-yela@hotmail.com','pbkdf2:sha256:260000$OVATCa0qfsmLU6qv$89c468b12f2c5d203b8b5042260d19838a589171bb5801fecb81e387a69025b1',2,'2023-02-06 10:56:46'),(3,'comercial','jcomercial@cootep.com.co','pbkdf2:sha256:260000$XovFn7EmdfESqiQj$35a95cf43d6ca1fba14ecfe02f251410c9cf6b8789285fe1200e327b0776d0b9',1,'2023-05-05 19:26:23'),(4,'asiscomercial','asistentecomercial@cootep.com.co','pbkdf2:sha256:260000$8aVq5El0z4suTfmE$7ddbd30c361707f5f38d71963d58352e74ea009243418403d33fe2cd8e45bf36',1,'2023-05-05 19:31:45'),(6,'MOTOAMAZONAS','Wilifredy@hotmail.com','pbkdf2:sha256:260000$5a0J3xk6aW5N6jfE$b18cf20b7e96b84edf85ad0fcad7f4c8e38aff0ce33f9802818ecd235947f5e3',2,'2023-05-15 20:04:11'),(7,'PAPELERIAUNICA','launicamocoa@hotmail.com','pbkdf2:sha256:260000$eQolA11YLnQJkNZg$085a2d1b4e44a68155f25fb4ef688cec93268151a93831d63ccc5d6d262dfed8',2,'2023-05-15 22:10:33'),(8,'RIVERAFLOREZ','riverayflorezltda@gmail.com','pbkdf2:sha256:260000$EI7dIIuEi0lD8SKx$0d6802df776d5d0f50b5931cf6eda47bd74623785395982302e791fff790d2ea',2,'2023-05-15 22:11:48'),(9,'DISTRISUR','adistrisur@yahoo.es','pbkdf2:sha256:260000$X8SxW9rWhP8QhdKq$07bb48ce65d0ec371a9e41220b4cada9c990e9bbfe3a6da7bc624634b5ec1ae1',2,'2023-05-15 22:18:28'),(10,'LABODEGA','autoserviciolabodegalupe@hotmail.com','pbkdf2:sha256:260000$R23am7RkSfe69KlV$900df322fffed694eb447326e827656747ca4a4915ba761b05a2b19924152106',2,'2023-05-15 22:19:58'),(11,'JAMARC','ccjamarc@yahoo.es','pbkdf2:sha256:260000$EtojTWPOdrIKZuqY$a20f75cbb925cc99ed4a6cb21405f8c28926f3ff35d1cde24632bc35f737ff98',2,'2023-05-15 22:20:21'),(12,'CICLOMOCOA','ciclomocoaea11@hotmail.com','pbkdf2:sha256:260000$LwB8PSnxiEByM2R3$e775a538f323aac27f939677b17fabd5fdc58ec4552b9b857e5226460792d8b1',2,'2023-05-15 22:21:12'),(13,'MAQUINAGRO','contabilidad@maquinagro.com','pbkdf2:sha256:260000$5YIlNcRJRQjd16Yf$6831b8a9610b35779994a2ec73d9c1e133a6c67b389b931323b2877f0238109f',2,'2023-05-15 22:21:47'),(14,'SURTIPASTO','contabilidaddarwin@gmail.com','pbkdf2:sha256:260000$1QLA9AWAKr5Hc9P8$680d73e0543a3627b22ffd51157b65ff44caa4303bdf3f9d6de18576c6c10cc5',2,'2023-05-15 22:22:39'),(15,'HONDAMAQUINAGRO','contabilidadmaquinagro@yahoo.es','pbkdf2:sha256:260000$JppExDmHkmqxNO2V$e5ab2957401d83ed9206bb1fcbb23d91c473e424001fbc8f5817fe60d4852b78',2,'2023-05-15 22:23:44'),(16,'TATIFARMACIA','derly.1984@hotmail.com','pbkdf2:sha256:260000$Czf7Pwqy5HgzKIc1$09b32f4736ecdb7e04976c6e5d49f398bad305322d6ec6b203897705a48be2b9',2,'2023-05-15 22:25:10'),(17,'TECNICELL','elfadedelosdaddy@hotmail.com','pbkdf2:sha256:260000$jtpSQ6aFgXT9jDPi$63f9c62ed989c5e888b75e5de466828c8491eabaffea316f5f7207036affeb1f',2,'2023-05-15 22:25:35'),(18,'ESTETIKANUEVAFORMA','francy.gordillo@hotmail.com','pbkdf2:sha256:260000$srdK6Dgk3jNNn7R2$a2da551a35ffc560fa087c659589229b5a6a5cc5f2460014877b6e1bc835d019',2,'2023-05-15 22:27:27'),(19,'ITP1','itputumayo@itp.edu.co','pbkdf2:sha256:260000$PUs3wMRiTT9AAQGt$61b3ecd687b9bb8140d5b4f4bf09f0334e261b4cb4a37be01671330f26a8c427',2,'2023-05-15 22:28:08'),(20,'TECCEL','jhonrb2704@gmail.com','pbkdf2:sha256:260000$vRpb8x3nOP45g6LJ$67bc3f64f1cfbea0b077e118427d3331b5e6c8a66b2792cbb1aab1c429d30955',2,'2023-05-15 22:28:40'),(21,'AKTMEGAMOTOR','megamotorakt@hotmail.com','pbkdf2:sha256:260000$7anE9uTA8qlhO1gZ$09ef515e4a17eb9b21e455fd57095257642100802664c60f46b51dc46198c0a6',2,'2023-05-15 22:29:17'),(22,'ODONTOLOGAICVO','odontologaicvo@hotmail.com','pbkdf2:sha256:260000$L3xfaR2vRpGJg09Y$e74f9e56b9e714f2bf71ecfd2940244923f8ae9cb99280d41c077eff4027db54',2,'2023-05-15 22:31:22'),(23,'MUNDOMUEBLES','silviatnguino27@gmail.com','pbkdf2:sha256:260000$U8wOD73WYjnKaL0T$1da1dd9bd7b12f577736ba9832545b7eeb10fc667e0f2d7bf0c19f5f2967c8e1',2,'2023-05-15 22:31:52'),(24,'SION','sion.conest@gmail.com','pbkdf2:sha256:260000$yFNLCtWLU1TVz1Gj$c28e422ad1643517f7097f6533fcfa116a229eae146f431658605d1d12b14b37',2,'2023-05-15 22:32:13'),(25,'VARIEDADESMAYE','veronica232001@hotmail.com','pbkdf2:sha256:260000$Sd8N3WVr3tLPOzXL$767647f20e9cdcd523d48d77212cbc4cab8d90dd3b9dd920e0efba7f99c1bafa',2,'2023-05-15 22:32:44');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-24 17:05:46
