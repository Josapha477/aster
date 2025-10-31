# Plateforme Sociale - Application Web

## Vue d'ensemble
Application web de réseau social avec fonctionnalités de partage de contenu média et de vente de produits. Construite avec Django REST Framework pour le backend et Vue.js (CDN) pour le frontend.

## État actuel du projet
- **Date de création**: 31 octobre 2025
- **Stack technique**: Django 5.2.7, Django REST Framework, Vue.js 3, Tailwind CSS, Axios
- **Base de données**: SQLite (développement)
- **Authentification**: JWT (Simple JWT)

## Architecture du projet

### Backend (Django)
- **Models**: ProfilUser, PostUserMedia, PostUserVente
- **API Endpoints**:
  - `/api/register/` - Inscription utilisateur
  - `/api/login/` - Connexion avec JWT
  - `/api/logout/` - Déconnexion
  - `/api/profil/` - Gestion du profil utilisateur
  - `/api/posts/media/` - Posts média (liste et création)
  - `/api/posts/vente/` - Posts vente (liste et création)
  - `/api/my-posts/` - Posts de l'utilisateur connecté

### Frontend (Vue.js)
- **Pages**:
  - Login - Authentification utilisateur
  - Register - Inscription avec création automatique de profil
  - Home - Fil d'actualité avec posts média et vente
  - Profil - Gestion du profil et création de posts
- **Design**: Responsive avec Tailwind CSS
- **Navigation**: Menu desktop et mobile avec état d'authentification

## Fonctionnalités

### Authentification
- Inscription avec création automatique de profil
- Connexion avec tokens JWT
- Gestion de session avec localStorage
- Déconnexion avec suppression des tokens

### Profil Utilisateur
- Photo de profil (upload d'images)
- Bio personnalisée (max 50 caractères)
- Visualisation des posts personnels

### Posts Média
- Upload d'images
- Description textuelle
- Affichage public dans le fil d'actualité
- Attribution par utilisateur

### Posts Vente
- Upload d'image du produit
- Description et prix (FCFA)
- Numéro WhatsApp pour contact
- Lien direct vers WhatsApp
- Affichage public dans le fil d'actualité

## Configuration

### Médias
- **MEDIA_URL**: `/media/`
- **MEDIA_ROOT**: `media/`
- **Uploads**: profil/, imgM/, imgV/

### CORS
- Configuré pour permettre toutes les origines en développement

### JWT
- Access token: 24 heures
- Refresh token: 7 jours

## Modifications récentes
- 31 octobre 2025: Création initiale du projet avec tous les modèles, API et interface utilisateur complète
- 31 octobre 2025: Ajout de rest_framework_simplejwt.token_blacklist pour permettre la déconnexion sécurisée avec blacklist des tokens JWT
- 31 octobre 2025: Configuration complète de l'interface admin Django pour gérer les utilisateurs, profils et posts

## Préférences utilisateur
- Framework: Django REST Framework
- Frontend: Vue.js via CDN (pas de build)
- CSS: Tailwind CSS via CDN
- Requêtes HTTP: Axios
- Design: Responsive mobile-first
