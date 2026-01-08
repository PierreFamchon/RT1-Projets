-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost	Database: sae23
-- ------------------------------------------------------
-- Server version    8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BlocsCompetences`
--

DROP TABLE IF EXISTS `BlocsCompetences`;
/*!40101 SET @saved_cs_client 	= @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BlocsCompetences` (
  `id` int NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BlocsCompetences`
--

LOCK TABLES `BlocsCompetences` WRITE;
/*!40000 ALTER TABLE `BlocsCompetences` DISABLE KEYS */;
INSERT INTO `BlocsCompetences` VALUES (1,'Administrer les réseaux et l internet'),(2,'Connecter les entreprises et les usagers'),(3,'Créer des outils et applications informatique pour les unités d enseignement');
/*!40000 ALTER TABLE `BlocsCompetences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Competences`
--

DROP TABLE IF EXISTS `Competences`;
/*!40101 SET @saved_cs_client 	= @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Competences` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(500) DEFAULT NULL,
  `bloc_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bloc_id` (`bloc_id`),
  CONSTRAINT `Competences_ibfk_1` FOREIGN KEY (`bloc_id`) REFERENCES `BlocsCompetences` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Competences`
--

LOCK TABLES `Competences` WRITE;
/*!40000 ALTER TABLE `Competences` DISABLE KEYS */;
INSERT INTO `Competences` VALUES (1,'1. Maîtriser les lois fondamentales de l électricité afin d’intervenir sur des équipements de réseaux et télécommunications',1),(2,'2. Configurer les fonctions de base du réseau local',1),(3,'3. Maîtriser les rôles et les principes fondamentaux des systèmes d exploitation afin d interagir avec ceux ci pour la configuration et l administration des réseaux et services fournis',1),(4,'4. Identifier les dysfonctionnements du réseau local et savoir les signaler',1),(5,'5. Installer un poste client, expliquer la procédure mise en place',1),(6,'6. Mesurer, analyser et commenter les signaux',2),(7,'7. Caractériser des systèmes de transmissions élémentaires et découvrir la modélisation mathématique de leur fonctionnement',2),(8,'8. Déployer des supports de transmission',2),(9,'9. Connecter les systèmes de ToIP',2),(10,'10. Communiquer avec un tiers (client, collaborateur...) et adapter son discours et sa langue à son interlocuteur',2),(11,'11. Utiliser un système informatique et ses outils',3),(12,'12. Lire, exécuter, corriger et modifier un programme',3),(13,'13. Traduire un algorithme, dans un langage et pour un environnement donné',3),(14,'14. Connaître l’architecture et les technologies d’un site Web',3),(15,'15. Choisir les mécanismes de gestion de données adaptés au développement de l outil et argumenter ses choix',3),(16,'16. S intégrer dans un environnement propice au développement et au travail collaboratif',3),(17,'17. Test',NULL),(18,'17. Test',NULL);
/*!40000 ALTER TABLE `Competences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CompetencesNiveaux`
--

DROP TABLE IF EXISTS `CompetencesNiveaux`;
/*!40101 SET @saved_cs_client 	= @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CompetencesNiveaux` (
  `competence_id` int NOT NULL,
  `niveau_id` int NOT NULL,
  PRIMARY KEY (`competence_id`,`niveau_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CompetencesNiveaux`
--

LOCK TABLES `CompetencesNiveaux` WRITE;
/*!40000 ALTER TABLE `CompetencesNiveaux` DISABLE KEYS */;
INSERT INTO `CompetencesNiveaux` VALUES (1,2),(2,2),(3,3),(4,2),(5,3),(6,1),(7,2),(8,2),(9,2),(10,2),(11,1),(12,2),(13,3),(14,3),(15,2),(16,1),(17,1),(18,1);
/*!40000 ALTER TABLE `CompetencesNiveaux` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NiveauxAcquisition`
--

DROP TABLE IF EXISTS `NiveauxAcquisition`;
/*!40101 SET @saved_cs_client 	= @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NiveauxAcquisition` (
  `id` int NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NiveauxAcquisition`
--

LOCK TABLES `NiveauxAcquisition` WRITE;
/*!40000 ALTER TABLE `NiveauxAcquisition` DISABLE KEYS */;
INSERT INTO `NiveauxAcquisition` VALUES (1,'Non acquis'),(2,'En cours d’acquisition'),(3,'Acquis');
/*!40000 ALTER TABLE `NiveauxAcquisition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client 	= @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `mot_de_passe` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','progtr00');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-03 11:14:14

